import requests
import streamlit as st
from sqlmodel import Session, select, and_
from models import Register, engine

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ChatBot
if st.session_state.logged_in:
    st.title("🎉 Welcome to ChatBot 🤖 " + st.session_state.username)

    if "user_messages" not in st.session_state:
        st.session_state.user_messages = []
    if "ai_messages" not in st.session_state:
        st.session_state.ai_messages = []

    url = "https://apifreellm.com/api/chat"
    headers = {
            "Content-Type": "application/json"
    }
    data = {
            "message": "Hello, Who are you?"
    }

    user_text = st.chat_input("say something...")
    if user_text is not None:
        
        data = {
            "message": user_text
        }
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        if result.get("status") == "success":
            print("Request OK ")
        else:
            st.info("Server is busy!")

        st.session_state.user_messages.append(user_text)
        st.session_state.ai_messages.append(result["response"])

        
        for ai,user in zip(st.session_state.ai_messages, st.session_state.user_messages):
            st.write("🧑🏼‍💻"+user)
            st.write(ai)

# Register / Login
else:
    selected_option = st.radio(
        "Please choose:",
        ["Log in", "Register"],
        horizontal=True,
        key="login_register_switch"
    )

    # Login
    if selected_option == "Log in":
        st.subheader("🔑 Login to your account")
        with st.form("login_form"):
            username = st.text_input("Username:", key="login_username")
            password = st.text_input("Password:", type="password", key="login_password")
            login_btn = st.form_submit_button("Login")

            if login_btn:
                with Session(engine) as session:
                    statement = select(Register).where(and_(
                        Register.username == username,
                        Register.password == password
                    ))
                    result = session.exec(statement).first()
                    if result:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.success("✅ Login successful")
                        st.rerun()  # going to chatbot part.
                    else:
                        st.error("❌ Invalid username or password")

    # Register
    elif selected_option == "Register":
        st.subheader("📝 Register new user")
        with st.form("register_form"):
            user_name = st.text_input("Username:", key="register_username")
            email = st.text_input("Email:", key="register_email")
            password = st.text_input("Password:", type="password", key="register_password")
            password_repeat = st.text_input("Repeat Password:", type="password", key="register_confirm_password")
            register_btn = st.form_submit_button("Register")

            if register_btn:
                if password != password_repeat:
                    st.error("❌ Passwords do not match!")
                else:
                    new_user = Register(username=user_name, email=email, password=password)
                    with Session(engine) as session:
                        session.add(new_user)
                        session.commit()
                        st.success("✅ Registered successfully! You can log in now.")
