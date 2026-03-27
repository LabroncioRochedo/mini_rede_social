from fastapi import FastAPI
from database.connection import engine,Base
from projeto_mini_rede_social.routers import auth
from models import user_model,private_chat_model,like_model,global_chat_model,friend_model,friend_request_model,comment_model

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)


#uvicorn main:app --reload