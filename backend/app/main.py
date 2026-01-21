from fastapi import FastAPI
from backend.app.database import Base, engine
from backend.app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ShopIntel Backend")

app.include_router(auth.router)
