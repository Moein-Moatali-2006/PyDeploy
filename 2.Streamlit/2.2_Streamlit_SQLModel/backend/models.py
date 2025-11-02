from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    ai_id: Optional[int] = Field(default=None, foreign_key="ai.id")
    sender: str 
    text: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
    education: Optional[str] = None

    messages: List["Message"] = Relationship(back_populates="user")


class AI(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_name: Optional[str] = None

    messages: List["Message"] = Relationship(back_populates="ai")



Message.user = Relationship(back_populates="messages")
Message.ai = Relationship(back_populates="messages")


