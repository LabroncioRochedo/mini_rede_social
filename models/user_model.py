from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship
from database.connection import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    senha = Column(String)

    global_chat = relationship("GlobalChat", back_populates="user")
    like = relationship("Like", back_populates="user")
    comment = relationship("Comment", back_populates="user")
    mensagens_enviadas = relationship("PrivateChat",foreign_keys="PrivateChat.remetente_id",back_populates="remetente")
    mensagens_recebidas = relationship("PrivateChat",foreign_keys="PrivateChat.destinatario_id",back_populates="destinatario")
    requests_enviados = relationship("FriendRequest",foreign_keys="FriendRequest.remetente_id",back_populates="remetente")
    requests_recebidos = relationship("FriendRequest",foreign_keys="FriendRequest.destinatario_id",back_populates="destinatario")
    amizades_1 = relationship("Friend",foreign_keys="Friend.user1_id",back_populates="usuario_1")
    amizades_2 = relationship("Friend",foreign_keys="Friend.user2_id",back_populates="usuario_2")
