from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from backend.database import get_session
from backend.models import User

router = APIRouter()


@router.post("/register")
def register_user(
    username: str,
    email: str,
    first_name: str = "",
    last_name: str = "",
    session: Session = Depends(get_session),
):
    existing_user = session.exec(select(User).where(User.username == username)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    user = User(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": "User registered successfully", "user_id": user.id}


@router.post("/login")
def login_user(username: str, email: str, session: Session = Depends(get_session)):
    """Login user if username and email match."""
    user = session.exec(
        select(User).where(User.username == username, User.email == email)
    ).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or email",
        )

    return {"message": "Login successful", "user_id": user.id}
