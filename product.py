from fastapi import APIRouter, HTTPException, Path
from typing import List
from app.schemas.product import Product

router = APIRouter()

@router.post("/products")
def create_product(product: Product):
    # Lógica para criar um novo produto
    return {"message": "Product created successfully"}

@router.get("/products", response_model=List[Product])
def list_products():
    # Lógica para listar todos os produtos
    return []

@router.get("/products/{id}", response_model=Product)
def get_product(id: str = Path(...)):
    # Lógica para buscar um produto pelo ID
    return {}

@router.put("/products/{id}", response_model=Product)
def update_product(id: str = Path(...), product: Product):
    # Lógica para atualizar um produto pelo ID
    return {}

@router.delete("/products/{id}", status_code=204)
def delete_product(id: str = Path(...)):
    # Lógica para deletar um produto pelo ID
    return {}

