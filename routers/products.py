from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message":"producto no encontrado"}})

products_list = ["product 1","product 2",
                 "product 3","product 4","product 5"]

@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]
