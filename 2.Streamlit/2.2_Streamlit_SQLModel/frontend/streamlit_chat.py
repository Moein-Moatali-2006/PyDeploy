import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000" 

st.set_page_config(page_title="ChatVibe", page_icon="🤖", layout="wide")
st.title("💬 ChatVibe Chat")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Please log in first!")
    st.stop()

user_id = st.session_state["user_id"]

def load_history():
    response = requests.get(f"{API_URL}/history/{user_id}")
    if response.status_code == 200:
        return response.json()
    return []

history = load_history()

for msg in history:
    if msg["sender"] == "user":
        st.markdown(f"**You:** {msg['text']}")
    else:
        st.markdown(f"**AI:** {msg['text']}")

st.markdown("---")

message = st.text_input("Type your message here:")

if st.button("Send") and message:
    payload = {"user_id": user_id, "message": message}
    response = requests.post(f"{API_URL}/chat/", params=payload)

    if response.status_code == 200:
        data = response.json()
        st.markdown(f"**You:** {data['user']}")
        st.markdown(f"**AI:** {data['ai']}")
    else:
        st.error("Failed to send message.")
