from fastapi import FastAPI
from backend.app.database import Base, engine
from backend.app.routes import auth, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ShopIntel Backend")

app.include_router(auth.router)
app.include_router(users.router)
