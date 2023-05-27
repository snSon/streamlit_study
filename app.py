import streamlit as st

def add_symbol(symbol):
    input_text = st.session_state["input_text"]
    input_text += symbol
    st.session_state["input_text"] = input_text

def main():
    st.title("기호 지원")

    if "input_text" not in st.session_state:
        st.session_state["input_text"] = ""

    # Symbol buttons
    st.write("Click a symbol to add:")
    symbols = ["+", "-", "*", "/", "^", "()", "√", "sin", "cos", "tan", "log", "ln"]
    button_col = st.beta_columns(len(symbols))  # 기호 버튼을 가로로 출력하기 위한 열 생성
    for i, symbol in enumerate(symbols):
        button_text = f"{symbol}"
        if button_col[i].button(button_text):
            add_symbol(symbol)

    # 문제 입력
    st.header("문제 입력")
    question = st.text_area("문제를 입력하세요", height=100)

    # 문제풀이 입력
    st.header("문제풀이 입력")
    solution = st.text_area("문제풀이를 입력하세요", height=300)

    # 백엔드에서 받아온 정답유무와 맞는 풀이 출력
    if st.button("정답 확인"):
        is_correct, correct_solution = check_answer(solution)  # Assuming `check_answer` is a function that returns (is_correct, correct_solution)
        if is_correct:
            st.success("맞았어요!!")
        else:
            show_solution = st.checkbox("풀이 확인")
            st.error("틀렸어요!!")
            if show_solution:
                st.info(f"맞는 풀이: {correct_solution}")

if __name__ == "__main__":
    main()
