from fastapi import FastAPI
from routers import products,users

app = FastAPI()

#ROUTER
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return  "Hello World"


@app.get("/url")
async def url():
    return {"url":"http://juanchocor.github.com/python"}

#url local: htto://127.0.0.1:8000

