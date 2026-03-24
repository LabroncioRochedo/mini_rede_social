from models.user_model import Usuario
from security.hash_senha import criar_hash_senha,verificar_hash_senha
from fastapi import HTTPException
from security.tokens import gerar_acess_token,gerar_refresh_token

def criar_usuario(usuario,db):

    hash_senha = criar_hash_senha(usuario.senha)
    try:
        novo_usuario = Usuario(
            nome=usuario.nome,
            senha=hash_senha
        )
        db.add(novo_usuario)
        db.commit()
    except:
        raise HTTPException(status_code=422, detail="usuaria ja existente")
    return {"msg":"conta criada"}

def login_usuario(usuario,db):

    dados = db.query(Usuario).filter(Usuario.nome == usuario.nome).first()

    if not dados:
        raise HTTPException(status_code=404, detail="usuario ou senha incorretos")

    if not verificar_hash_senha(usuario.senha,dados.senha):
        raise HTTPException(status_code=404, detail="usuario ou senha incorretos")
    
    acess_token = gerar_acess_token(dados.id)
    refresh_token = gerar_refresh_token(dados.id)


    return {"acess_token": acess_token,"refresh_token":refresh_token}