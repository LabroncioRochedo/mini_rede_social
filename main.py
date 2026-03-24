from fastapi import FastAPI
from database.connection import engine,Base
from routers import user
from models import user_model

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)


#uvicorn main:app --reload