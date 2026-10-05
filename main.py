from fastapi import FastAPI
from pydantic import BaseModel 

class Product(BaseModel):
    name: str
    price: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, this is my first API"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id, "name": "Product number " + str(product_id)}

@app.post("/products")
def create_product(product: Product):
    return {"message": "Product created", "product": product}