import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/auth" 

st.set_page_config(page_title="ChatVibe Login", page_icon="💬", layout="centered")
st.title("💬 ChatVibe Login")

mode = st.radio("Select mode:", ["Login", "Register"], horizontal=True)

username = st.text_input("Username")
email = st.text_input("Email")
first_name = ""
last_name = ""

if mode == "Register":
    first_name = st.text_input("First name (optional)")
    last_name = st.text_input("Last name (optional)")

if st.button(mode):
    if not username or not email:
        st.warning("Please enter username and email.")
    else:
        if mode == "Register":
            response = requests.post(
                f"{API_URL}/register",
                params={
                    "username": username,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                },
            )
        else:
            response = requests.post(
                f"{API_URL}/login",
                params={"username": username, "email": email},
            )

        if response.status_code == 200:
            data = response.json()
            st.success(data["message"])
            st.session_state["user_id"] = data["user_id"]
            st.session_state["username"] = username
            st.session_state["logged_in"] = True
            st.switch_page("frontend/streamlit_chat.py") 
        else:
            st.error(response.json().get("detail", "Something went wrong."))
