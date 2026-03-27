from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from database.connection import Base
from sqlalchemy.orm import relationship
import datetime

class Friend(Base):

    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    user1_id = Column(Integer, ForeignKey("usuarios.id"))
    user2_id = Column(Integer, ForeignKey("usuarios.id"))
    conteudo = Column(String)
    data_de_envio = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("Usuario", back_populates="friend")