import streamlit as st

def check_answer(solution):
    # 정답 확인 로직 구현
    # 예시로 정답을 True로 가정하고 반환
    is_correct = True
    correct_solution = "정답"
    return is_correct, correct_solution

def add_symbol_question(symbol):
    input_text_question = st.session_state.get("input_text_question", "")
    input_text_question += symbol
    st.session_state["input_text_question"] = input_text_question

def add_symbol_solution(symbol):
    input_text_solution = st.session_state.get("input_text_solution", "")
    input_text_solution += symbol
    st.session_state["input_text_solution"] = input_text_solution

def main():
    st.title("고등학교 수학 풀이 검증")

    if "input_text_question" not in st.session_state:
        st.session_state["input_text_question"] = ""
        st.session_state["input_text_solution"] = ""

    # Symbol buttons for question
    st.write("Click a symbol to add to question:")
    symbols_question = ["+", "-", "*", "/", "^", "√"]
    for symbol in symbols_question:
        button_text = f"Add {symbol}"
        if st.button(button_text, key=symbol):
            add_symbol_question(symbol)

    # 문제 입력
    st.header("문제 입력")
    question = st.text_area("문제를 입력하세요", height=100, value=st.session_state["input_text_question"])

    # Symbol buttons for solution
    st.write("Click a symbol to add to solution:")
    symbols_solution = ["sin", "cos", "tan", "log", "ln", "∫", "dx", "d/dx", "df/dx"]
    for symbol in symbols_solution:
        button_text = f"Add {symbol}"
        if st.button(button_text, key=symbol):
            add_symbol_solution(symbol)

    # 문제풀이 입력
    st.header("문제풀이 입력")
    solution = st.text_area("문제풀이를 입력하세요", height=300, value=st.session_state["input_text_solution"])

    # 정답 확인
    if st.button("Check Answer"):
        is_correct, correct_solution = check_answer(solution)
        if is_correct:
            st.success("Correct!")
        else:
            show_solution = st.checkbox("Show Solution")
            st.error("Incorrect!")
            if show_solution:
                st.info(f"Correct Solution: {correct_solution}")

if __name__ == "__main__":
    main()
