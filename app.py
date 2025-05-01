import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, World! 🚀")

name = st.text_input("What's your name?")
if name:
    st.success(f"Welcome, {name}!")