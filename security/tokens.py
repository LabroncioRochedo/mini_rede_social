from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

secret = SECRET_KEY

security = HTTPBearer()

def gerar_acess_token(user_id):
    payload = {"user_id": user_id,"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
    token = jwt.encode(payload,secret,algorithm="HS256")
    return token

def checar_token(credentials = Depends(security)):

    token = credentials.credentials

    try:
        payload = jwt.decode(token,secret,algorithms=["HS256"])
        user_id = payload.get("user_id")
        return user_id
    except:
        raise HTTPException(status_code=401, detail="Token inválido")

def gerar_refresh_token(usuario_id):

    payload = {"user_id": usuario_id,"exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)}
    token = jwt.encode(payload, secret, algorithm="HS256")

    return token