from sqlalchemy import Column,Integer,ForeignKey
from database.connection import Base
from sqlalchemy.orm import relationship

class Like(Base):

    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    global_chat_id = Column(Integer, ForeignKey("global_chat.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("usuarios.id"))

    global_chat = relationship("Global_chat", back_populates="like")
    user = relationship("Usuario", back_populates="like")