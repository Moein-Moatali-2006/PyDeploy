from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from backend.database import init_db, get_session
from backend.models import User, AI, Message
from backend.auth_routes import router as auth_router
import requests
from datetime import datetime

app = FastAPI(title="ChatBot")
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/chat/")
def chat_with_ai(user_id: int, message: str, session: Session = Depends(get_session)):
    user_msg = Message(
        user_id=user_id,
        sender="user",
        text=message,
        timestamp=datetime.utcnow(),
    )
    session.add(user_msg)
    session.commit()

    api_url = "https://api-inference.huggingface.co/models/gpt2"  
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  
    payload = {"inputs": message}

    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=15)
        ai_reply = response.json()[0]["generated_text"]
    except Exception as e:
        ai_reply = f"[Error contacting AI API: {e}]"

    ai_msg = Message(
        ai_id=1,
        sender="ai",
        text=ai_reply,
        timestamp=datetime.utcnow(),
    )
    session.add(ai_msg)
    session.commit()

    return {"user": message, "ai": ai_reply}


@app.get("/history/{user_id}")
def get_chat_history(user_id: int, session: Session = Depends(get_session)):
    messages = session.exec(
        select(Message).where(Message.user_id == user_id).order_by(Message.timestamp)
    ).all()
    return messages
