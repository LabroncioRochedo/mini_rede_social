from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship
from database.connection import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    senha = Column(String)

    private_chat = relationship("Private_chat", back_populates="user")
    global_chat = relationship("Global_chat", back_populates="user")
    like = relationship("Like", back_populates="user")
    comment = relationship("Comment", back_populates="user")
    friend_request = relationship("Friend_request", back_populates="user")
    friend = relationship("Friend", back_populates="user")