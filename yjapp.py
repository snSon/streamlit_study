import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.title('Math Proof')

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Tutorial', 'Start'], 
        icons=['house', 'caret-right-square', 'pencil'], menu_icon="cast", default_index=0)
    selected

if selected == 'Home':
    image = Image.open('math.jpg')
    st.image(image, width=800)

if selected == 'Tutorial':
    st.write("다 만들고 사용 영상 넣기")

if selected == 'Start':
    # 기능X
    sort = st.radio(
        "select",
        ("수학1", "수학2", "미적분", "확률과통계", "벡터")
    )
    st.write('')

    st.subheader("Enter Question")
    
    # 기호 지원
    def add_symbol1(symbol):
        question = st.session_state["question"]
        question += symbol
        st.session_state["question"] = question

    if "question" not in st.session_state:
        st.session_state["question"] = ""
    
    symbol1 = st.selectbox("기호 선택", ("+", "-", "×", "÷", "√", "^", "sin", "cos", "tan", "log", "∫"), key="symbol1")
    button1 = st.button("기호 추가", key="button1")

    if button1:
        add_symbol1(symbol1)
    
    # 문제 입력
    question = st.session_state["question"]
    question = st.text_input("문제 입력", question, key="question")
    st.write("The mathematical formula to prove is", '"', question, '"')
    st.write('')

    st.subheader('Enter Question Solution')

    def add_symbol2(symbol):
        solution = st.session_state["solution"]
        solution += symbol
        st.session_state["solution"] = solution

    if "solution" not in st.session_state:
        st.session_state["solution"] = ""
    
    symbol2 = st.selectbox("기호 선택", ("+", "-", "×", "÷", "√", "^", "sin", "cos", "tan", "log", "∫"), key="symbol2")
    button2 = st.button("기호 추가", key="button2")

    if button2:
        add_symbol2(symbol2)
    
    # 문제 풀이 입력
    solution = st.session_state["solution"]
    solution = st.text_input("문제풀이 입력", solution, key="solution")
    st.write('')
    
    st.subheader("Check Question Solution")

    # 정답 확인
    def check_answer(solution):
    # 정답 확인 로직을 구현합니다.
    # 풀이가 맞으면 True를 반환하고, 틀리면 False를 반환합니다.
    # 이 예시에서는 정답을 "정답"으로 설정하고 풀이가 "정답"과 일치하면 맞다고 판별합니다.
        return True
    
    if st.button("풀이 확인"):
        is_correct = check_answer(solution)
        if is_correct:
            st.success("정답입니다!")
        else:
            st.error("틀렸습니다. 다시 확인해보세요.")
            show_solution = st.checkbox("풀이를 확인하시겠습니까?")
            if show_solution:
                st.info("올바른 풀이: 정답")  
