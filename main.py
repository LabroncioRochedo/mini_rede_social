from fastapi import FastAPI
from database.connection import engine,Base
from models import comment_model, friend_model, friend_request_model, global_chat_model, like_model, private_chat_model
from routers import auth, comment, friend, friend_request, global_chat, like, private_chat
from routers import user
from models import user_model

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


#source venv/bin/activate
