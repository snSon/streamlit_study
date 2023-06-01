from PIL import Image
from streamlit_option_menu import option_menu
import streamlit as st
import openai


# 기호 지원
def add_symbol1(symbol):
    question = st.session_state["question"]
    question += symbol
    st.session_state["question"] = question

def add_symbol2(symbol):
    solution = st.session_state["solution"]
    solution += symbol
    st.session_state["solution"] = solution


API_KEY = "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"
@st.cache_resource
def get_openai_chat_completion_model(question, solution):  # type: ignore
    openai.api_key = API_KEY
    completion = openai.ChatCompletion.create(  # type: ignore
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "아래에 주어진 question에 대한 solution이 맞는지 틀렸는지 판별해라."},
            {"role": "user", "content": "solution이 틀렸을 때 '맞겠냐'라고 답해라. solution이 맞았을 때 '좀치네'라고 답해라."},
            {"role": "user", "content": "solution이 틀렸을 때 '맞겠냐'라고 답하고 '&&&'를 출력하고 올바른 풀이를 제공해라."},
            {"role": "user", "content": question},
            {"role": "user", "content": solution}
        ],
        temperature=0.8,
        max_tokens=2048
    )
    return completion["choices"][0]["message"]["content"].encode("utf-8").decode()  # type: ignore

def check_answer(question, solution):  # type: ignore
    model = get_openai_chat_completion_model(question, solution)  # ChatCompletion 객체 가져오기 #type: ignore
    return model  # type: ignore


st.title('수학 증명 계산기')

with st.sidebar:
    selected = option_menu("목록", ["계산기", "계산기 가이드"],
        icons=['house', 'caret-right-square'], menu_icon="cast", default_index=0)
    selected

if selected == '계산기':

    sort = st.radio(
        "select",
        ("수학1", "수학2", "미적분", "확률과통계", "벡터")
    )

    st.subheader("문제 입력")

    if "question" not in st.session_state:
        st.session_state["question"] = ""

    # 문제 입력
    question = st.session_state["question"]
    question = st.text_input("문제 입력", question)
    gptQuestion = "question: " + question


    symbol1 = ["√", "^", "sin", "cos", "tan", "log", "∫"]
    button_col1 = st.columns(5)
    for i, symbol in enumerate(symbol1):
        if button_col1[i % 5].button(symbol, key=f"button1_{i}"):
            add_symbol1(symbol)


    st.subheader('문제 풀이 입력')

    if "solution" not in st.session_state:
        st.session_state["solution"] = ""

    # 문제 풀이 입력
    solution = st.session_state["solution"]
    solution = st.text_input("문제풀이 입력", solution)
    gptSolution = "solution: " + solution

    symbol2 = ["√", "^", "sin", "cos", "tan", "log", "∫"]
    button_col2 = st.columns(5)
    for i, symbol in enumerate(symbol2):
        if button_col2[i % 5].button(symbol, key=f"button2_{i}"):
            add_symbol2(symbol)


    st.subheader("정답 확인")

    is_correct = check_answer(gptQuestion, gptSolution)
    sub = is_correct.split("&&&")

    if st.button("OX 확인"):
        if question and solution:  # type: ignore
            st.write(is_correct)
            if "좀치네" in is_correct:
                st.success("정답입니다!")
            elif "맞겠냐" in is_correct:
                st.error("틀렸습니다. 다시 확인해보세요.")
            else:
                st.write("멍청한 gpt")

    show_solution = st.checkbox("풀이를 확인하시겠습니까?")
    if show_solution:
        st.write(sub[1])
