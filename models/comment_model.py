from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from database.connection import Base
from sqlalchemy.orm import relationship
import datetime

class Comment(Base):

    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    global_chat_id = Column(Integer, ForeignKey("global_chat.id"))
    user_id = Column(Integer, ForeignKey("usuarios.id"))
    conteudo = Column(String)
    data_de_envio = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("Usuario", back_populates="comment")
    global_chat = relationship("Global_chat", back_populates="comment")