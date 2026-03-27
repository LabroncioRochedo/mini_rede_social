from fastapi import FastAPI
from database.connection import engine,Base
from projeto_mini_rede_social.routers import auth,global_chat,like,comment
from models import user_model,private_chat_model,like_model,global_chat_model,friend_model,friend_request_model,comment_model

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(global_chat.router)
app.include_router(like.router)
app.include_router(comment.router)


#uvicorn main:app --reload