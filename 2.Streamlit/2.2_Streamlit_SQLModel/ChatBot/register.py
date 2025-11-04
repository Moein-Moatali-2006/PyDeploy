import streamlit as st


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
        st.text_input("Username: ", key="register_username")
        st.text_input("Email:", key="register_email")
        st.text_input("Password: " , type="password", key="register_password")
        st.text_input("Repeat Password:", type="password", key="register_confirm_password")
        st.form_submit_button("Register")
