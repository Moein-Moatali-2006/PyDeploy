from typing import Optional
from sqlmodel import SQLModel, Field, create_engine

class Register(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(primary_key=True, index=True)
    username: str = None
    email: Optional[str] = None
    password: str = None


DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)