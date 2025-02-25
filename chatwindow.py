import streamlit as st

st.title("Chat Window")

with st.chat_message("assistant"):
    st.markdown("Hello I am AI Assistant")

with st.chat_message("human"):
    st.markdown("I am planning trip to dubai")

message=st.chat_input("Enter Your Message")

if message:
    with st.chat_message("human"):
      st.markdown(message)