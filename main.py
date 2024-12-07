from chatbot import ChatBot
from openai import OpenAI
import streamlit as st
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

st.title("Math assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "username" not in st.session_state:
    st.header("Siz tizimga kirmagansiz")
    
else:
    st.header(f"Salom {st.session_state.username}")

with st.sidebar:
    openai_model = st.radio(
        "Modelni tanlang",
        ["gpt-4o-mini", "gpt-4", "gpt-4-turbo"],
        index=0,
    )

    user_api_key = st.text_input("OpenAI API Key")
    st.button("Saqlash")
    client = ChatBot(api_key=user_api_key, model_name=openai_model)

    logout_button = st.button("Tizimdan chiqish")
    if logout_button and "username" in st.session_state:
        del st.session_state.username
        st.session_state.messages = []
        st.rerun()

if user_api_key:

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Savolingizni shu yerga kiriting?"):
        st.session_state.messages.append({"role": "human", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = client.get_response(history=st.session_state.messages, question=prompt)
            st.markdown(response)

        st.session_state.messages.append({"role": "ai", "content": response})
else:
    st.error("API_KEY kiritilmagan")