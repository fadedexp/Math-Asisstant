import streamlit as st
import json

st.title("Login Page")
username = st.text_input("Username").lower()
password = st.text_input("Password", type="password")
signup_button = st.button("Create account")
login_button = st.button("Login")

if signup_button:
    try:
        with open("user_data/users.json", "r") as json_file:
            loaded_data = json.load(json_file)
    except FileNotFoundError:
        loaded_data = []

    for items in loaded_data:
        if username == items["username"]:
            st.error("This username is already taken!")
            break
    else:
        dct = {
            "username": username,
            "password": password
        }
        loaded_data.append(dct)
        with open("user_data/users.json", "w") as json_file:
            json.dump(loaded_data, json_file, indent=4)
        
        st.success("Account Created!")

if login_button:
    try:
        with open("user_data/users.json", "r") as json_file:
            loaded_data = json.load(json_file)
    except FileNotFoundError:
        st.error("No users found. Please create an account first.")
        loaded_data = []

    for items in loaded_data:
        if username == items["username"] and password == items["password"]:
            st.session_state.username = username.capitalize()
            st.success("Login successful!")
            break
    else:
        st.error("Invalid username or password!")
