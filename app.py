import streamlit as st

def add_symbol(symbol, input_key):
    input_text = st.session_state[input_key]
    input_text += symbol
    st.session_state[input_key] = input_text

def main():
    st.title("Symbol Addition")

    if "input_text_question" not in st.session_state:
        st.session_state["input_text_question"] = ""

    if "input_text_solution" not in st.session_state:
        st.session_state["input_text_solution"] = ""

    # Symbol buttons
    st.write("Click a symbol to add:")
    symbols = ["+", "-", "*", "/", "^", "()", "√", "sin", "cos", "tan", "log", "ln", "∫", "dx", "d/dx", "df/dx"]

    button_cols = st.beta_columns(4)  # 4개의 열 생성

    for i, symbol in enumerate(symbols):
        button_text = f"Add {symbol}"
        button_col = button_cols[i // 4]  # 열 선택: 4개 버튼마다 열 변경

        with button_col:
            if st.button(button_text, key=symbol):  # 각 버튼에 고유한 키(key) 설정
                add_symbol(symbol, "input_text_question")
                add_symbol(symbol, "input_text_solution")

    # 문제 입력
    st.header("문제 입력")
    question = st.text_area("문제를 입력하세요", height=100, key="input_text_question")

    # 문제풀이 입력
    st.header("문제풀이 입력")
    solution = st.text_area("문제풀이를 입력하세요", height=300, key="input_text_solution")

    # 백엔드에서 받아온 정답유무와 맞는 풀이 출력
    if st.button("Check Answer"):
        is_correct, correct_solution = check_answer(solution)  # Assuming `check_answer` is a function that returns (is_correct, correct_solution)
        if is_correct:
            st.success("Correct!")
        else:
            show_solution = st.checkbox("Show Solution")
            st.error("Incorrect!")
            if show_solution:
                st.info(f"Correct Solution: {correct_solution}")

if __name__ == "__main__":
    main()
