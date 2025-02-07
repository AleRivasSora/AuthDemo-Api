from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field, field_validator
from passlib.context import CryptContext
import re

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name must be between 3 and 50 characters")
    email: EmailStr = Field(..., description="Invalid email address")
    password: str = Field(..., min_length=8, max_length=20, description="Password must be at least 8 characters and no more than 20 characters")

    @field_validator('email')
    def email_length(cls, v):
        if len(v) > 50:
            raise ValueError('Email must be no more than 50 characters')
        return v

    @field_validator('password')
    def password_complexity(cls, v):
        if ' ' in v:
            raise ValueError('Password cannot contain spaces')
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$', v):
            raise ValueError('Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character')
        return v

class UserOut(BaseModel):
    name: str
    email: EmailStr

class LoginData(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20, description="Password must be at least 8 characters and no more than 20 characters")

users = {}

@app.post("/register", response_model=UserOut)
async def create_user(user: User):
    if any(u.email == user.email for u in users.values()):
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    users[user.email] = user
    return {"name": user.name, "email": user.email, "message": "User created successfully"}

@app.post("/login")
async def login_user(login_data: LoginData):
    user = users.get(login_data.email)
    if user and pwd_context.verify(login_data.password, user.password):
        return {"message": "Logged in successfully"}
    raise HTTPException(status_code=401, detail="Incorrect email or password")