from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="ShopIntel API")

# ---- In-memory DB (auto-update, no MySQL delay) ----
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 25000},
]

class Product(BaseModel):
    id: Optional[int]
    name: str
    price: float

# READ + SEARCH
@app.get("/api/products", response_model=List[Product])
def get_products(search: Optional[str] = None):
    if search:
        return [p for p in products if search.lower() in p["name"].lower()]
    return products

# CREATE
@app.post("/api/products", response_model=Product)
def create_product(product: Product):
    product.id = products[-1]["id"] + 1 if products else 1
    products.append(product.dict())
    return product

# UPDATE
@app.put("/api/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    for p in products:
        if p["id"] == product_id:
            p["name"] = product.name
            p["price"] = product.price
            return p
    raise HTTPException(status_code=404, detail="Product not found")

# DELETE
@app.delete("/api/products/{product_id}")
def delete_product(product_id: int):
    global products
    products = [p for p in products if p["id"] != product_id]
    return {"message": "Deleted"}
