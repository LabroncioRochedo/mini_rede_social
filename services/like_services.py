from models.like_model import Like
from models.global_chat_model import GlobalChat
from fastapi import HTTPException

def enviar_like(user_id,post_id,db):
    verificar_post = db.query(GlobalChat).filter(GlobalChat.id == post_id.post_id).first()

    if not verificar_post:
        raise HTTPException(status_code=404,detail="post nao encontrado")
    
    verificar_se_curtiu = db.query(Like).filter(Like.global_chat_id == post_id.post_id, Like.user_id == user_id).firts()

    if not verificar_se_curtiu:

        new = Like(
            user_id=user_id,
            global_chat_id=post_id
        )

        db.add(new)
        db.commit()

        total_likes = db.query(Like).filter(Like.global_chat_id == post_id).count()
        return {"like":True, "total_likes": total_likes}
    
    db.delete(verificar_se_curtiu)
    db.commit()
    return {"like":False}

