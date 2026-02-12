from sqlmodel import Field, Session, SQLModel, create_engine


class Contact(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    phone: str
    email: str
    text: str | None = None

class Register(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    email: str
    username: str
    age: int
    city: str
    country: str
    password: str
    jointime: str

def make_database(bool):
    if bool:
        engine = create_engine("sqlite:///./database.db")
        SQLModel.metadata.create_all(engine)
        print("Database has made.")
        return engine
