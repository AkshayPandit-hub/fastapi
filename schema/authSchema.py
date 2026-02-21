from pydantic import BaseModel,Field

class registerUserRequest(BaseModel):
    
    first_name: str = Field(validation_alias="first name")
    last_name : str = Field(validation_alias="last name")
    email : str = Field(validation_alias="Email Address")
    password : str 
    
    model_config = {"from_attributes" : True}

class userResponse(BaseModel):
    
    id: int = Field(serialization_alias="user_id")
    first_name: str = Field(serialization_alias="first name")
    last_name : str = Field(serialization_alias="last name")
    email : str = Field(serialization_alias="Email Address")
    roles : list = []
    
    
    model_config = {"from_attributes" : True}