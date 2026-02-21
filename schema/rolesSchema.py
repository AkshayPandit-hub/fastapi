from pydantic import BaseModel

class add_role_request(BaseModel):
    role_name: str
    description :str


class role_response(BaseModel):
    id: int
    role_name: str
    description :str