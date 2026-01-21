from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit

    products = db.query(Product).offset(offset).limit(limit).all()
    total = db.query(Product).count()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": products
    }
