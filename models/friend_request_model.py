from sqlalchemy import Column,Integer,ForeignKey,DateTime
from database.connection import Base
from sqlalchemy.orm import relationship
import datetime

class FriendRequest(Base):

    __tablename__ = "friend_request"

    id = Column(Integer, primary_key=True)
    remetente_id = Column(Integer, ForeignKey("usuarios.id"))
    destinatario_id = Column(Integer, ForeignKey("usuarios.id"))
    data_de_envio = Column(DateTime, default=datetime.datetime.utcnow)

    remetente = relationship("Usuario",foreign_keys=[remetente_id],back_populates="requests_enviados")
    destinatario = relationship("Usuario",foreign_keys=[destinatario_id],back_populates="requests_recebidos")