from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from config import Base

class Roles(Base):
    
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, unique=True)
    role_name = Column(String, unique=True)
    description = Column(String)
    
    users = relationship("UserRoles", back_populates="role")