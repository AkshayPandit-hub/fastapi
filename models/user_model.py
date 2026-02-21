from config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"
    
    id = Column(Integer,primary_key=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String,unique=True)
    hashed_password = Column(String)
    active_status = Column(Boolean,default=True)
    
    roles = relationship("UserRoles", back_populates="user")

    
    