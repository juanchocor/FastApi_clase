from fastapi import FastAPI, Depends,HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

user_db = {
    "juanchocor" : {
        "username": "juanhocor",
        "full_name": "Cordoba M",
        "email": "jazz1916@gmail.com",
        "disabled": False, 
        "password" : "123456"
    },
     "felipecho" : {
        "username": "Felipecho",
        "full_name": "Cortez M",
        "email": "feli1916@gmail.com",
        "disabled": False, 
        "password" : "23456"
    },
     "Ubaldo" : {
        "username": "Ubaldoche",
        "full_name": "Renteria M",
        "email": "Ubaldo1916@gmail.com",
        "disabled": False, 
        "password" : "123456"
    }
}

def search_user(username: str):
    if username in user_db:
        return UserDB(users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=401, detail="el usuario no es correcto"
        )




@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = user_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status, detail="el usuario no es correcto")

    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=400, detail="la contraseña no es correcta"
            )

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
