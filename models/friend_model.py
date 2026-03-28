from sqlalchemy import Column,Integer,ForeignKey
from database.connection import Base
from sqlalchemy.orm import relationship

class Friend(Base):

    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    user1_id = Column(Integer, ForeignKey("usuarios.id"))
    user2_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario_1 = relationship("Usuario",foreign_keys=[user1_id],back_populates="amizades_1")
    usuario_2 = relationship("Usuario",foreign_keys=[user2_id],back_populates="amizades_2")