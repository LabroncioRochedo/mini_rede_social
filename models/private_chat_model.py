from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from database.connection import Base
from sqlalchemy.orm import relationship
import datetime

class Private_chat(Base):

    __tablename__ = "private_chat"

    id = Column(Integer, primary_key=True)
    remetente_id = Column(Integer, ForeignKey("usuarios.id"))
    destinatario_id = Column(Integer, ForeignKey("usuarios.id"))
    conteudo = Column(String)
    data_de_envio = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("Usuario", back_populates="private_chat")