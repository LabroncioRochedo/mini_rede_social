from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from security.tokens import checar_token
from schemas.like_schemas import EnviarLike
from services.like_services import enviar_like

router = APIRouter(prefix="/like",dependencies=[Depends(checar_token)])

@router.post("/")
async def like(post_id: EnviarLike,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return enviar_like(user_id,post_id,db)