import streamlit as st

st.title("Proof Math")

with st.container():
   st.header("What is Question?")
   question = st.text_input("write here")

st.write(question)

with st.container():
   st.subheader("Proof Question")
   proof = st.text_input("proof")

click1 = st.button("1")
click2 = st.button("2")
click3 = st.button("3")

if click1:
   question += st.text_input("1")
  
st.wirte(question)
