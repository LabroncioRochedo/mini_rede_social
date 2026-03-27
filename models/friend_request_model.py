from sqlalchemy import Column,Integer,ForeignKey,DateTime
from database.connection import Base
from sqlalchemy.orm import relationship
import datetime

class Friend_request(Base):

    __tablename__ = "friend_request"

    id = Column(Integer, primary_key=True)
    remetente_id = Column(Integer, ForeignKey("usuarios.id"))
    destinatario_id = Column(Integer, ForeignKey("usuarios.id"))
    data_de_envio = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("Usuario", back_populates="friend_request")