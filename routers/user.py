from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from services.user_services import criar_usuario,login_usuario
from schemas.user_schemas import UsuarioCreat

router = APIRouter()

@router.post("/criar")
async def criar(usuario: UsuarioCreat, db: Session = Depends(get_db)):
    return criar_usuario(usuario,db)


@router.post("/login")
async def login(usuario: UsuarioCreat, db: Session = Depends(get_db)):
    return login_usuario(usuario,db)