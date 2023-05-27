import streamlit as st

def check_answer(solution):
    # 정답 확인 로직 구현
    # 예시로 정답을 True로 가정하고 반환
    is_correct = True
    correct_solution = "정답"
    return is_correct, correct_solution

def add_symbol(symbol):
    input_text_question = st.session_state.get("input_text_question", "")
    input_text_solution = st.session_state.get("input_text_solution", "")
    
    if st.session_state.get("is_question_input", False):
        input_text_question += symbol
        st.session_state["input_text_question"] = input_text_question
    elif st.session_state.get("is_solution_input", False):
        input_text_solution += symbol
        st.session_state["input_text_solution"] = input_text_solution

def main():
    st.title("고등학교 수학 풀이 검증")

    if "input_text_question" not in st.session_state:
        st.session_state["input_text_question"] = ""
        st.session_state["input_text_solution"] = ""
        st.session_state["is_question_input"] = False
        st.session_state["is_solution_input"] = False

    # Symbol buttons
    st.write("Click a symbol to add:")
    symbols = ["+", "-", "*", "/", "^", "√", "sin", "cos", "tan", "log", "ln", "∫", "dx", "d/dx", "df/dx"]
    for symbol in symbols:
        button_text = f"Add {symbol}"
        if st.button(button_text, key=symbol):
            add_symbol(symbol)

    # 문제 입력
    st.header("문제 입력")
    st.session_state["is_question_input"] = True
    question = st.text_area("문제를 입력하세요", height=100, value=st.session_state["input_text_question"])
    st.session_state["is_question_input"] = False

    # 문제풀이 입력
    st.header("문제풀이 입력")
    st.session_state["is_solution_input"] = True
    solution = st.text_area("문제풀이를 입력하세요", height=300, value=st.session_state["input_text_solution"])
    st.session_state["is_solution_input"] = False

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
