# ChatVibe - AI Chat Application

ChatVibe is a simple AI-powered chat application built using **Python**, **FastAPI**, **Streamlit**, and **SQLModel**. Users can register, log in, and chat with an AI. All conversations are saved in a SQLite database.

---

## Features

- User registration and login system
- AI-powered chat using external API (e.g., OpenAI or HuggingFace)
- Message history stored in SQLite database
- Clean and minimal frontend with Streamlit
- Secure endpoints using FastAPI

---

## Technologies Used

- Python 3.10+
- FastAPI
- Streamlit
- SQLModel (with SQLite)
- Requests (for communicating with AI API)

---

## Project Structure

```
chat-Bot/
├─ backend/
│  ├─ app.py             # FastAPI entrypoint
│  ├─ models.py          # SQLModel models (User, AI, Message)
│  ├─ db.py              # Database engine and session
│  ├─ auth_routes.py     # Registration and login endpoints
│  └─ chat_routes.py     # Chat endpoints (optional separate file)
├─ frontend/
│  ├─ streamlit_login.py # Streamlit login/register UI
│  └─ streamlit_chat.py  # Streamlit chat UI
└─ requirements.txt      # Python dependencies
```

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatvibe.git
cd chatBot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Setup

1. Run the FastAPI backend:
```bash
uvicorn backend.app:app --reload
```

2. Run the Streamlit frontend:
```bash
streamlit run frontend/streamlit_login.py
```

3. Open your browser at `http://localhost:8501`

---

## Usage

1. Register a new user or login with existing credentials.
2. After login, you'll be redirected to the chat interface.
3. Type a message and click **Send** to chat with the AI.
4. Your messages and AI responses are saved automatically in the database.

---

## AI API Integration

Currently, the application uses a placeholder API for AI responses. You can replace it with any AI service, such as OpenAI GPT or HuggingFace API.

Example in `app.py`:
```python
api_url = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
payload = {"inputs": message}
response = requests.post(api_url, headers=headers, json=payload)
ai_reply = response.json()[0]["generated_text"]
```

---

## License

This project is licensed under the MIT License.

---

## Author

Moein Moatali - [GitHub](https://github.com/yourusername)

