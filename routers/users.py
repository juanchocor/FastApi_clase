from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"])

#entidad users
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name="Juan", surname="juancho",url="http://juanchocor/github",age=35),
              User(id=2,name="David",surname="davichu",url="http://davicho/github",age=30),
              User(id=3,name="andres",surname="andrecho",url="http://andrecho/github",age=30)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Juan", "surname":"Juancho", "url": "http://juanchocor/github", "age":30},
            {"name": "David", "surname":"davichu", "url": "http://davicho/github","age":30},
            {"name": "Andres", "surname":"andrecho", "url": "http://andrecho/github","age":30}]


@router.get("/users")
async def users():
    return users_list
    
#path
@router.get("/user/{id}")
async def user(id: int):
    return search_user()

#query
@router.get("/user/")
async def user(id: int):
    return search_user(id)


#creamos con un POST un nuevo usuario que nos con diferencial del id PK 
#se añaden al paht una linea de status_code + el detail en el caso de error.
@router.post("/user/", response_model=User, status_code=201 )
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El usuario ya existe" )
        
    users_list.append(user)
    return user
    

#creacion del metodo PUT para actualizar datos.
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate (users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return { "error" : "no se ha actualizado el usuario"}
    else:
        return user 
    


#creacion del metodo DELETE para eliminar datos 
@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
           del users_list[index] 
           found = True

    if not found:
        return {"error":"No se ha eliminado el usuario"}
    


def search_user(id: int):
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return { "error" : "no se ha encontrado el usuario"}










    

