import streamlit as st

def add_symbol(symbol):
    input_text = st.session_state["input_text"]
    input_text += symbol
    st.session_state["input_text"] = input_text

def main():
    st.title("Symbol Addition")

    if "input_text" not in st.session_state:
        st.session_state["input_text"] = ""

    st.write("Click a symbol to add:")
    symbols = ["!", "@", "#", "$", "%"]
    button_row = st.empty()
    for symbol in symbols:
        button_text = f"Add {symbol}"
        button_row.button(button_text, key=symbol)  # 가로 형태로 버튼 출력


    # Input field
    input_text = st.session_state["input_text"]
    input_text = st.text_input("Input", input_text, key="input_text")
    st.write("Input text:", input_text)

    # 문제 입력
    st.header("문제 입력")
    question = st.text_area("문제를 입력하세요")

    # 문제풀이 입력
    st.header("문제풀이 입력")
    solution = st.text_area("문제풀이를 입력하세요")

    # 입력받은 문제와 문제풀이 출력
    st.header("입력받은 문제와 문제풀이")
    st.write("문제:", question)
    st.write("문제풀이:", solution)

if __name__ == "__main__":
    main()
