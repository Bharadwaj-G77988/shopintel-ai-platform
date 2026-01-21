from fastapi import FastAPI
from backend.app.database import Base, engine
from backend.app.routes import auth, users, admin, products

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ShopIntel Backend")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(products.router)
