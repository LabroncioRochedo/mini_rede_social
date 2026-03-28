from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from security.tokens import checar_token
from schemas.friend_schemas import DesfazerAmizade
from services.friend_services import ver_amigos,desfazer_amizade

router = APIRouter(prefix="/amigos",dependencies=[Depends(checar_token)])

@router.get("/")
async def listar(db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return ver_amigos(user_id,db)

@router.delete("/")
async def deletar(friend_id:DesfazerAmizade,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return desfazer_amizade(friend_id,user_id,db)