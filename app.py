import openai
import streamlit as st
from back import *
from streamlit_option_menu import option_menu

API_KEY = "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"

@st.cache_resource #type:ignore
def get_openai_chat_completion_model(question, solution):  # type: ignore
    openai.api_key = API_KEY
    completion = openai.ChatCompletion.create(  # type: ignore
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
            {"role": "user", "content": solution},
            {"role": "user", "content": "첫 번째 답변은 solution이 올바른 추론이면 '예', 올바른 추론이 아니면 '아니요'로 대답한다. 첫번째 답변이'아니요'일 때, solution을 '명제가 틀린 경우'는 따로 제시하고 마지막으로 올바른 solution을 제시한다."},
        ],
        temperature=0.3,
        max_tokens=2048
    )
    return completion["choices"][0]["message"]["content"].encode("utf-8").decode()  # type: ignore

def check_answer(question, solution):  # type: ignore
    model = get_openai_chat_completion_model(question, solution)  # ChatCompletion 객체 가져오기 #type: ignore
    return model  # type: ignore

# 기호 지원
def add_symbol1(symbol):
    question = st.session_state["question"]
    question += symbol
    st.session_state["question"] = question


def add_symbol2(symbol):
    solution = st.session_state["solution"]
    solution += symbol
    st.session_state["solution"] = solution


st.title('수학 증명 계산기')

with st.sidebar:
    selected = option_menu("목록", ["계산기", "가이드"],
                           icons=['calculator', 'caret-right-square'], menu_icon="cast", default_index=0)
    selected

if selected == '계산기':

    # 기능X
    sort = st.radio(
        "select",
        ("수학1", "수학2", "미적분", "확률과통계", "벡터")
    )
    st.write('')

    st.subheader("문제 입력")

    if "question" not in st.session_state:
        st.session_state["question"] = ""

    symbol1 = ["√", "∫", "∑", "∧", "∨", "¬", "→", "∀", "∃"]
    button_col1 = st.columns(5)
    for i, symbol in enumerate(symbol1):
        if button_col1[i % 5].button(symbol, key=f"button1_{i}"):
            add_symbol1(symbol)

    # 문제 입력
    question = st.session_state["question"]
    question = st.text_input("문제 입력", question, key="question")
    question = "question: " + question

    st.subheader('문제 풀이 입력')

    if "solution" not in st.session_state:
        st.session_state["solution"] = ""

    symbol2 = ["√", "∫", "∑", "∧", "∨", "¬", "→", "∀", "∃"]
    button_col2 = st.columns(5)
    for i, symbol in enumerate(symbol2):
        if button_col2[i % 5].button(symbol, key=f"button2_{i}"):
            add_symbol2(symbol)

    # 문제 풀이 입력
    solution = st.session_state["solution"]
    solution = st.text_area("문제풀이 입력", solution, key="solution", height=170)

    solution = "solution: " + solution

    st.subheader("정답 확인")

    if st.button("풀이 확인"):
        if question and solution:
            is_correct = check_answer(question, solution)  # type:ignore
            if ("아니요" or "올바르지 않습니다" or "잘못된") in is_correct:
                st.error("틀렸습니다. 다시 확인해보세요.")
                st.write(is_correct)  # type:ignore
            elif ("예" or "맞습니다") in is_correct:
                st.success("정답입니다!")
                st.write(is_correct)  # type:ignore
            else:
                st.write("멍청한 gpt")  # type:ignore
        else:
            st.warning("Please enter both the question and the solution.")

if selected == "가이드":
