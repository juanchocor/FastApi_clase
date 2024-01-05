from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    full_name: str
    email: str
    disabled: bool

user_db = {
    "juanchocor" : {
        "name": "Juan David",
        "full_name": "Cordoba M",
        "email": "jazz1916@gmail.com",
        "disabled": False, 
        "password" : "123456"
    },
     "felipecho" : {
        "name": "Felipe",
        "full_name": "Cortez M",
        "email": "feli1916@gmail.com",
        "disabled": False, 
        "password" : "23456"
    },
     "Ubaldo" : {
        "name": "Ubaldo",
        "full_name": "Renteria M",
        "email": "Ubaldo1916@gmail.com",
        "disabled": False, 
        "password" : "123456"
    }
}