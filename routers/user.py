from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from security.tokens import checar_token
from schemas.user_schemas import AcharUsuario,VerPostDoUsuario
from services.user_services import achar_usuario,ver_post_do_usuario

router = APIRouter(prefix="/usuario",dependencies=[Depends(checar_token)])

@router.post("/achar")
async def achar(nome: AcharUsuario,db: Session = Depends(get_db)):
    return achar_usuario(nome,db)

@router.post("/posts")
async def ver_post(user_id: VerPostDoUsuario,db: Session = Depends(get_db)):
    return ver_post_do_usuario(user_id,db)