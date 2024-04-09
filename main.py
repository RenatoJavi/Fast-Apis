# video tutorial https://www.youtube.com/watch?v=XPuRc1LItCI
from fastapi import FastAPI
from model.user_conection import UserConection
from schema.user_schema import UserSchema

app=FastAPI() 
conec = UserConection()
@app.get("/")
def root():
    #conec
    
    items = []
    for data in conec.read_todo(): # retornar en formato Json
        diccionario ={}
        diccionario ["id"] =data[0]
        diccionario ["name"] =data[1]
        diccionario ["phone"] =data[2]
        items.append(diccionario)
    
    return items

# 
@app.post("/api/insert")
def insert(user_data: UserSchema): # tipeo con Usershema
    data=user_data.dict() # Convierte el objeto Pydantic a un diccionario Python .json
    data.pop("id") # Elimina la clave 'id' del diccionario
    #print(data)
    conec.write(data) # estp me  permite escribir un nuevo dato en la base

@app.get("/api/user/{id}")    
def get_one (id: str):
    dicctionary ={} 
    data= conec.read_un_usuario(id) # me retorna el mismo valor de la BD, que le estamos pasando
    dicctionary ["id"] =data[0]
    dicctionary ["name"] =data[1]
    dicctionary ["phone"] =data[2]
    return dicctionary

@app.delete("/api/delete/{id}")
def delete_user(id:str):
    datos = conec.delete_usuario(id)
    
@app.put("/api/update/{id}") # actuaizar 
def actualizar(user_data: UserSchema, id:str) :
    data = user_data.dict()
    data["id"]=id
    conec.actualizar_usuario(data)
    
  
   # return {"mensaje":f"User con ID {id} eleiminado con exito"}