import streamlit as st

st.title('Image Processing App')

name= st.text_input("Enter Your Name:")

if st.button("Say Hello"):
    st.write(f"Hello {name},Welcome to AI Assistant")