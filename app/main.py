from fastapi import FastAPI
from app.controllers.user import router as user_router
from app.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_router)