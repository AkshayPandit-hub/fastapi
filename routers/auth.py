from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from config import db_dependency,create_token
from typing import Annotated
from schema import authSchema
from models import User, Roles, UserRoles
from passlib.context import CryptContext
import os , dotenv
from jose import jwt
from datetime import time, timedelta,timezone

auth_routers = APIRouter(
    prefix="/auth"
)
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')



@auth_routers.post("/login")
async def login_user(db:db_dependency, request_form:Annotated[OAuth2PasswordRequestForm,Depends()]):
    
    user = authenticate_user(db,request_form.username,request_form.password)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Wrong Credentials")

    return create_token(user)


@auth_routers.post("/register",response_model=authSchema.userResponse)
async def register_user(db:db_dependency, request:authSchema.registerUserRequest):
    
    if find_user_email(db, request.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User with this email already exist")
    
    user_data = User(
        first_name = request.first_name,
        last_name =request.last_name,
        email = request.email,
        hashed_password = bcrypt_context.hash(request.password)
        )
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data

def find_user_email(db:db_dependency,email:str) -> bool :
    user = db.query(User).filter(User.email == email).first()
    if user:
        return True
    return False

def authenticate_user(db:db_dependency,email:str, password:str):
    result = db.query(User).filter(User.email == email).first()
    if result:
        if bcrypt_context.verify(password,result.hashed_password):
            return result
    return None

    