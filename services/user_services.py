from models.user_model import Usuario
from models.global_chat_model import GlobalChat
from fastapi import HTTPException

def achar_usuario(nome,db):
    nomes = db.query(Usuario.id,Usuario.nome).filter(Usuario.nome.ilike(f"%{nome.nome}%")).all()

    if not nomes:
        raise HTTPException(status_code=404,detail="usuario nao encontrado")
    
    lista_nomes = []

    for a in nomes:
        lista_nomes.append(
            {"id": a.id,
            "nome": a.nome}
        )

    return lista_nomes

def ver_post_do_usuario(user_id,db):

    verificar_usuario = db.query(Usuario).filter(Usuario.id == user_id.user_id).first()

    if not verificar_usuario:
        raise HTTPException(status_code=404,detail="usuario nao encontrado")

    posts = db.query(GlobalChat).filter(GlobalChat.user_id == user_id.user_id).all()

    if not posts:
        return {"msg":"nenhum post encontrado"}
    
    return posts