# Streamlit Chatbot with Login/Register and LLM API

This project is a **web‑based chatbot application** built with **Streamlit** and **SQLModel** for login/register functionality.  
The chatbot connects to a **free LLM API** (e.g., ApiFreeLLM) to provide AI responses in real‑time.

---

## Features

- User **registration** and **login** system with SQLite database.
- Session‑based **chat interface** with message history.
- Integration with **LLM API** to generate AI responses.
- **Logout** button to end session and clear chat history.
- Clean UI using Streamlit’s chat message components.

---

## Screenshots

![Register]()  
![Login/Register]()  
![Chatbot]()

---

## Installation

1. Clone the repository:

```bash
git clone 
cd Chatbot
```

2. Install dependencies:

```bash
pip install ‑r requirements.txt
```

> **Note:** If you don’t have `requirements.txt`, install manually:
```bash
pip install streamlit sqlmodel requests
```

---

## Usage

1. Run the Streamlit app:

```bash
streamlit run main.py
```

2. Open the browser at `http://localhost:8501`.

3. **Register** a new user or **login** with existing credentials.

4. Start chatting with the AI chatbot.

5. Use **Logout** to end the session and clear chat history.

---

## Database

- This project uses **SQLite** via SQLModel.
- The database file will be created automatically when you run the app.
- Table: `Register` with columns:
  - `id` (primary key)
  - `username`
  - `email`
  - `password`

---

## LLM API

- The chatbot is connected to a free LLM API (e.g., ApiFreeLLM).  
- Messages are sent via **POST requests** and responses are displayed in real‑time.

---

## Folder Structure

```
Chatbot/
│
├── main.py           # Main Streamlit app
├── models.py         # SQLModel database models
├── database.db       # SQLite database file (auto‑created)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## License

This project is **MIT Licensed** — feel free to use and modify.

---

## Contact

Created by **Moein Moatali**  
Email: MoeinMoatali@gmail.com 


