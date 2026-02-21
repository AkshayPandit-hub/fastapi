from fastapi import APIRouter
from .roles import find_role_by_id
from .users import find_user_by_id
from models import UserRoles

from config import db_dependency

user_role_routers = APIRouter(prefix="/userRole")

@user_role_routers.post("/assign/{user_id}")
async def assign_role_to_user(user_id:int, role_id:int,db:db_dependency):
    try :
        user =find_user_by_id(db,user_id)
        role = find_role_by_id(db,role_id)
        
        userRole = UserRoles(user_id = user.id,role_id = role.id)
        db.add(userRole)
        db.commit()
        db.refresh(userRole)
        return userRole
    except Exception as e:
        return f"Exception occured : {e}"