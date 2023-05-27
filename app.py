import streamlit as st

def check_answer(solution):
    # 정답 확인 로직을 구현합니다.
    # 풀이가 맞으면 True를 반환하고, 틀리면 False를 반환합니다.
    # 이 예시에서는 정답을 "정답"으로 설정하고 풀이가 "정답"과 일치하면 맞다고 판별합니다.
    return solution == "정답"

def main():
    st.title("고등학교 수학 문제 풀이 판별")

    # 문제 입력
    st.header("문제 입력")
    question = st.text_area("문제를 입력하세요", height=100)

    # 문제 풀이 입력
    st.header("문제 풀이 입력")
    solution = st.text_area("문제 풀이를 입력하세요", height=300)

    # 기호 지원
    st.sidebar.header("기호 지원")
    symbol = st.sidebar.selectbox("기호를 선택하세요", ("+", "-", "×", "÷", "√", "^", "sin", "cos", "tan", "log", "∫"))

    # 문제나 문제 풀이 입력란에 기호 추가
    if st.sidebar.button("기호 추가"):
        if st.text_input == question:
            question += symbol
        elif st.text_input == solution:
            solution += symbol

    # 정답 확인
    if st.button("풀이 확인"):
        is_correct = check_answer(solution)
        if is_correct:
            st.success("정답입니다!")
        else:
            show_solution = st.checkbox("풀이를 확인하시겠습니까?")
            st.error("틀렸습니다. 다시 확인해보세요.")
            if show_solution:
                st.info("올바른 풀이: 정답")

if __name__ == "__main__":
    main()
