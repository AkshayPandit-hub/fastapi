from fastapi import APIRouter,status,HTTPException
from config import db_dependency
from models import User
from schema import userResponse
user_routers = APIRouter(prefix="/users")

@user_routers.get("/",response_model=list[userResponse])
async def get_users(db:db_dependency, user_id:int | None = None):
    if user_id is None:
        return db.query(User).all()
    
    user = find_user_by_id
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return [user]

def find_user_by_id(db:db_dependency,user_id:int):
    return db.query(User).filter(User.id == user_id).first()
    