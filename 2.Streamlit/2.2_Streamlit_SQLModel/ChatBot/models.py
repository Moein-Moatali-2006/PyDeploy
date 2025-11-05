from typing import Optional
from sqlmodel import SQLModel, Field, create_engine

class Register(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)