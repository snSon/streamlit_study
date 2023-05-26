import streamlit as st

def add_symbol(symbol):
    input_text = st.session_state["input_text"]
    input_text += symbol
    st.session_state["input_text"] = input_text

def main():
    st.title("Symbol Addition")

    if "input_text" not in st.session_state:
        st.session_state["input_text"] = ""

    # Symbol buttons
    st.write("Click a symbol to add:")
    symbols = ["!", "@", "#", "$", "%"]
    for symbol in symbols:
        button_text = f"Add {symbol}"
        if st.button(button_text):
            add_symbol(symbol)

    # Input field
    input_text = st.session_state["input_text"]
    input_text = st.text_input("Input", input_text, key="input_text")
    st.write("Input text:", input_text)

if __name__ == "__main__":
    main()
