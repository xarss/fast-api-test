from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.controllers.user_controller import router as user_router
from app.controllers.role_controller import router as role_router
from app.controllers.auth_controller import router as auth_router
from app.db import Base, SessionLocal, engine
from app.seeds.role_seed import seed_roles
from app.seeds.user_seed import seed_users

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"OpenAPI URL: {app.root_path}/{app.docs_url}")
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

app.include_router(user_router)
app.include_router(role_router)
app.include_router(auth_router)