from pydantic import BaseModel,Field
from typing import List, Optional

class registerUserRequest(BaseModel):
    
    first_name: str = Field(validation_alias="first name")
    last_name : str = Field(validation_alias="last name")
    email : str = Field(validation_alias="Email Address")
    password : str 
    
    model_config = {"from_attributes" : True}

class RoleDetail(BaseModel):
    id: int
    role_name: str
    
    model_config = {"from_attributes" : True}

class UserRoleDetail(BaseModel):
    id: int
    status: bool
    role: RoleDetail
    
    model_config = {"from_attributes" : True}

class userResponse(BaseModel):
    
    id: int = Field(serialization_alias="user_id")
    first_name: str = Field(serialization_alias="first name")
    last_name : str = Field(serialization_alias="last name")
    email : str = Field(serialization_alias="Email Address")
    roles: List[UserRoleDetail] = []
    
    model_config = {"from_attributes" : True}