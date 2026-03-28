from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from database.connection import Base
from sqlalchemy.orm import relationship
import datetime

class PrivateChat(Base):

    __tablename__ = "private_chat"

    id = Column(Integer, primary_key=True)
    remetente_id = Column(Integer, ForeignKey("usuarios.id"))
    destinatario_id = Column(Integer, ForeignKey("usuarios.id"))
    conteudo = Column(String)
    data_de_envio = Column(DateTime, default=datetime.datetime.utcnow)

    remetente = relationship("Usuario",foreign_keys=[remetente_id],back_populates="mensagens_enviadas")
    destinatario = relationship("Usuario",foreign_keys=[destinatario_id],back_populates="mensagens_recebidas")