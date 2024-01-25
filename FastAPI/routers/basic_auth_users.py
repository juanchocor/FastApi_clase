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
    

#se crea bases de datos tipo json
users_db = {
    "juanchocor" : {
        "username": "juanchocor",
        "full_name": "Juan David Cordoba M",
        "email": "jazz1916@gmail.com",
        "disabled": False, 
        "password" : "123456"
    },
     "felipecho" : {
        "username": "felipecho",
        "full_name": "Felipe Cortez M",
        "email": "feli1916@gmail.com",
        "disabled": False, 
        "password" : "23456"
    },
     "Ubaldoc" : {
        "username": "Ubaldoc",
        "full_name": "Ubaldo Renteria M",
        "email": "Ubaldo1916@gmail.com",
        "disabled": False, 
        "password" : "123456"
    }
}

#para motrar solo los datos de usuario sin contraseña se crea la funcion search_user_db
def seach_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def seach_user(username: str):
    if username in users_db:
        return User(**users_db[username])

    
async def current_user(token: str = Depends(oauth2)):
    user = seach_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autentificacion inavlidas", 
            headers={"WWW-Authenticate": "bearer"})
    
    if user.disabled:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario incorrecto")
    return user 


@app.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = seach_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user 
