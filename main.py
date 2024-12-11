from chatbot import ChatBot
from openai import OpenAI
import streamlit as st
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


with st.sidebar:
    language = st.radio(
        "Tilni tanlang / Выберите язык",
        ["O'zbek tili", "Русский язык"], 
        index=0
    )
    st.session_state.language = language

    if st.session_state.language == "O'zbek tili":
        # st.markdown("### Matematik yordamchi bilan ishlash uchun savolingizni kiriting.")
        header_label = "Siz tizimga kirmagansiz!"
        greeting_label = "Salom"
        model_label = "Modelni tanlang"
        api_key_label = "OpenAI API Kaliti"
        save_button_label = "Saqlash"
        logout_button_label = "Tizimdan chiqish"
        chat_input_placeholder = "Savolingizni shu yerga kiriting:"
        api_key_error = "API_KEY kiritilmagan"
    else:
        # st.markdown("### Введите ваш вопрос для математического помощника.")
        header_label = "Вы не вошли в систему!"
        greeting_label = "Привет"
        model_label = "Выберите модель"
        api_key_label = "Ключ API OpenAI"
        save_button_label = "Сохранить"
        logout_button_label = "Выйти из системы"
        chat_input_placeholder = "Введите ваш вопрос здесь."
        api_key_error = "Ключ API не введен"

    openai_model = st.radio(
        model_label,
        ["gpt-4o-mini", "gpt-4", "gpt-4-turbo"],
        index=0,
    )

    user_api_key = st.text_input(api_key_label)
    st.button(save_button_label)
    client = ChatBot(api_key=user_api_key, model_name=openai_model)

    logout_button = st.button(logout_button_label)
    if logout_button and "username" in st.session_state:
        del st.session_state.username
        st.session_state.messages = []
        st.rerun()

st.title("Math assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "username" not in st.session_state:
    st.header(header_label)
else:
    st.header(f"{greeting_label} {st.session_state.username}")

if user_api_key:

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input(chat_input_placeholder):
        st.session_state.messages.append({"role": "human", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = client.get_response(history=st.session_state.messages, question=prompt, language=st.session_state.language)
            st.markdown(response)

        st.session_state.messages.append({"role": "ai", "content": response})
else:
    st.error(api_key_error)