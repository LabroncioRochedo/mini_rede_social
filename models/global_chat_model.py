from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from database.connection import Base
from sqlalchemy.orm import relationship
import datetime

class Global_chat(Base):

    __tablename__ = "global_chat"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("usuarios.id"))
    conteudo = Column(String)
    likes = Column(Integer)
    comments = Column(Integer)
    data_de_envio = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("Usuario", back_populates="global_chat")
    like = relationship("Like", back_populates="global_chat")
    comment = relationship("Comment", back_populates="global_chat")