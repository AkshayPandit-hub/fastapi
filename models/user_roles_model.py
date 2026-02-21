from sqlalchemy import Integer, Column,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from .user_model import User
from .roles_model import Roles
from config import Base

class UserRoles(Base):
    __tablename__="user_roles"
    
    id = Column(Integer,primary_key=True,unique=True)
    user_id = Column(Integer,ForeignKey(User.id))
    role_id = Column(Integer,ForeignKey(Roles.id))
    status = Column(Boolean, default=True)
    
    user = relationship("User", back_populates="roles")
    role = relationship("Roles", back_populates="users")