import streamlit as st

@st.cache_data
def sum(x,y):
   return x+y

st.title("Proof Math")

with st.container():
   st.header("What is Question?")
   question = st.text_input("write here")

st.write(question)

with st.container():
   st.subheader("Proof Question")
   proof = st.text_input("proof")

st.write(proof)

click1 = st.button("1")
click2 = st.button("2")
click3 = st.button("3")

if click1:
   sub =  st.text_input("calc")

final_proof = st.cache_data(proof, sub)

st.write(final_proof)
