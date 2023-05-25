import streamlit as st

st.title("Proof Math")

st.header("What is Question?")
question = st.text_input("write here")

st.subheader("Proof Question")
proof = st.text_input("proof")

click1 = st.button(st.markdown("[$\sqrt{x}$]"))
click2 = st.button("2")
click3 = st.button("3")


