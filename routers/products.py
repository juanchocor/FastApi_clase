from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
async def products():
    return ["product1","product2","product3","product4","product5"]