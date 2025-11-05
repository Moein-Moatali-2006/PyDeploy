import streamlit as st
from sqlmodel import Session
from models import Register, engine


selected_option = st.radio(
    "Please Choice:",
    ["log in", "Register"],
    horizontal=True, 
    key="login_register_switch" 
)
# login
if selected_option == "log in":
    st.subheader("🔑login to your account")
    with st.form("login_form"):
        st.text_input("Username:", key="login_username")
        st.text_input("Password:", type="password", key="login_password")
        st.form_submit_button("login")
#Register
elif selected_option == "Register":
    st.subheader("📝 Register new user")
    with st.form("register_form"):
        user_name = st.text_input("Username: ", key="register_username")
        email = st.text_input("Email:", key="register_email")
        password = st.text_input("Password: " , type="password", key="register_password")
        password_repeat = st.text_input("Repeat Password:", type="password", key="register_confirm_password")
        if password != password_repeat:
            st.error("Password!")
        register_btn = st.form_submit_button("Register")

        if register_btn:
           new_user = Register(username=user_name, email=email, password=password)

           with Session(engine) as session:
               session.add(new_user)
               session.commit() 
               st.success("Registered ✅")
