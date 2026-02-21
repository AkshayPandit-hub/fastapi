from fastapi import APIRouter,status,HTTPException,Query
from config import db_dependency
from models import Roles
from schema import *
from sqlalchemy import func
from typing import Annotated

roles_router = APIRouter(
    prefix="/roles"
)

@roles_router.get("/") 
async def get_roles(db:db_dependency, role_id : Annotated[int , Query()] = None): 
    if role_id is None:
        return db.query(Roles).all()
    return find_role_by_id(db,role_id)

def find_role_by_id(db:db_dependency, role_id:int):
    role = db.query(Roles).filter(Roles.id == role_id).first()
    if role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return role
@roles_router.post("/",response_model=rolesSchema.role_response)
async def add_role(db:db_dependency, request:add_role_request):
    role = find_role(db,request.role_name)
    if isinstance(role,bool):
        role = Roles(role_name = request.role_name,description = request.description)
        db.add(role)
        db.commit()
        db.refresh(role)
        return role
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Role already exist with this name")

def find_role(db:db_dependency,role_name:str):
    role = db.query(Roles).filter(func.lower(Roles.role_name) == func.lower(role_name)).first()
    if role is None:
        return False
    return role

@roles_router.get("/by_role_name")
async def find_by_role_name(db:db_dependency,role_name:str):
    role = find_role(db,role_name)
    if isinstance(role, bool):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Role not found with the name {role_name}")
    return role


