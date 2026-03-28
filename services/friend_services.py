from models.friend_model import Friend
from models.user_model import Usuario
from sqlalchemy import or_,and_
from fastapi import HTTPException

def ver_amigos(user_id,db):
    amigos = db.query(Friend).filter(or_(Friend.user1_id == user_id,Friend.user2_id == user_id)).all()
    
    if not amigos:
        return {"msg":"nenhuma amizade encontrada"}
    
    amigos_ids = [a.user1_id if a.user2_id == user_id else a.user2_id for a in amigos]

    usuarios = db.query(Usuario.id,Usuario.nome).filter(Usuario.id.in_(amigos_ids)).all()
    
    lista_usuarios = []

    for usuario in usuarios:

        lista_usuarios.append(
            {"id": usuario.id,
             "nome": usuario.nome}
        )

    return lista_usuarios

def desfazer_amizade(friend_id,user_id,db):
    amigo = db.query(Friend).filter(or_(and_(Friend.user1_id == friend_id.friend_id,Friend.user2_id == user_id),and_(Friend.user2_id == friend_id.friend_id,Friend.user1_id == user_id))).first()

    if not amigo:
        raise HTTPException(status_code=404,detail="amigo nao encontrado")
    
    db.delete(amigo)
    db.commit()

    return {"msg":"amizade desfeita"}