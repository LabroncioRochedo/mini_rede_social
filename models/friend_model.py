from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from database.connection import Base
from sqlalchemy.orm import relationship
import datetime

class Friend(Base):

    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    user1_id = Column(Integer, ForeignKey("usuarios.id"))
    user2_id = Column(Integer, ForeignKey("usuarios.id"))

    user = relationship("Usuario", back_populates="friend")