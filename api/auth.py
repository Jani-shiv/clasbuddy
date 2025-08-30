from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from db.database import get_db
from auth.authentication import (
    authenticate_user,
    create_access_token,
    get_password_hash,
    get_current_active_user,
    get_user
)
from models.user import User
from config import settings

router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    full_name: str = None
    student_id: str = None
    year: str = None
    major: str = None


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    full_name: str = None
    is_active: bool
    is_verified: bool
    student_id: str = None
    year: str = None
    major: str = None
    
    class Config:
        from_attributes = True


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    # Check if user already exists
    if get_user(db, email=user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Check if username already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )
    
    # Create new user
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        full_name=user.full_name,
        student_id=user.student_id,
        year=user.year,
        major=user.major
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Login and get access token"""
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    """Get current user profile"""
    return current_user


@router.put("/me", response_model=UserResponse)
def update_user_profile(
    full_name: str = None,
    bio: str = None,
    year: str = None,
    major: str = None,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update current user profile"""
    if full_name is not None:
        current_user.full_name = full_name
    if bio is not None:
        current_user.bio = bio
    if year is not None:
        current_user.year = year
    if major is not None:
        current_user.major = major
    
    db.commit()
    db.refresh(current_user)
    return current_user
