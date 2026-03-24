from sqlalchemy import Column,String,Integer
from database.connection import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    senha = Column(String)