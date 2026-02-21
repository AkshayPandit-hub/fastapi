from typing import Annotated,Generator
from sqlalchemy.orm import Session
from .db_config import SessionLocal
from fastapi import Depends,status,HTTPException
from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
import os
from models import User
from fastapi.security import OAuth2PasswordBearer


secret_key = os.getenv("SECRET_KEY")
algorithms = 'HS256'

Oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]


def create_token(user : User, expires_delta:timedelta = timedelta(minutes=20) ):
    
    payload = {
        "sub":user.id,
        "email" : user.email,
        "name" : user.first_name +" " + user.last_name,
        "roles" : user.roles
    }
    expires = datetime.now(timezone.utc)+ expires_delta
    payload.update({"expires": expires.timestamp()})
    
    return jwt.encode(claims=payload,key=secret_key,algorithm=algorithms)

def get_current_user(token: Annotated[str,Depends(Oauth2_bearer)]):
    try:
        payload = jwt.decode(token=token,key=secret_key,algorithms=algorithms)
        userid = payload.get("sub")
        email = payload.get('email')
        roles = payload.get('roles')

        if userid is None or email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
        return{
            "userid": userid,
            "email" :email,
            "roles" : roles
        }
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")


