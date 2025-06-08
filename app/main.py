from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.controllers.user import router as user_router
from app.controllers.role import router as role_router
from app.db import Base, SessionLocal, engine
from app.seeds.role import seed_roles
from app.seeds.user import seed_users

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(app.docs_url)
    db = SessionLocal()
    seed_roles(db)
    seed_users(db)
    db.close()
    yield

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Example Project",
    lifespan=lifespan
)

app.include_router(user_router, tags=["User"])
app.include_router(role_router, tags=["Role"])