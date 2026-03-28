from fastapi import FastAPI
from database.connection import engine,Base
from projeto_mini_rede_social.routers import auth,global_chat,like,comment,user,friend,friend_request,private_chat
from models import user_model,private_chat_model,like_model,global_chat_model,friend_model,friend_request_model,comment_model

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(global_chat.router)
app.include_router(like.router)
app.include_router(comment.router)
app.include_router(friend.router)
app.include_router(user.router)
app.include_router(friend_request.router)
app.include_router(private_chat.router)


#uvicorn main:app --reload