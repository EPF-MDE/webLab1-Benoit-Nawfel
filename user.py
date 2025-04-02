from fastapi import FastAPI,HTTPException,Body
from pydantic import BaseModel, Field
from typing import List,Optional

app = FastAPI()
class User(BaseModel):
    id: Optional[int] = None
    name: str
    username: str
    password: str
    gender: str

user_db: List[User] = []

@app.get("/users/{dynamic_param}")
async def read_all_users(dynamic_param):
    return {"dynamic_param":dynamic_param}

@app.post("/users/create_user")
async def create_user(new_user: User):
    new_user.id = len(user_db) + 1
    user_db.append(new_user)
    return {"message" : "User created successfully", "user": new_user}

@app.get("/users")
async def read_all_users():
    all_users=[user for user in user_db]
    return all_users

@app.put("/users/update_user/{user_id}")
async def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(user_db):
        if user.id == user.id:
            updated_user.id = user.id
            user_db[i] = updated_user
            return {"message" : f"user with id {user_id} has been updated", "book": updated_user}
    raise HTTPException(status_code=404, detail=f"Book with id {user_id} not found")

@app.delete("/users/update_user/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(user_db):
        if user.id == user.id:
            del user_db[i] 
            return {"message" : f"book with id {user_id} has been deleted"}
    raise HTTPException(status_code=404, detail=f"Book with id {user_id} not found")

@app.patch("/users/patch/{user_id}")
async def patch_user(user_id: int, patch_data: User):
    stored_user_data = None
    for user in user_db:
        if user.id == user.id:
            stored_user_data = user
            update_data = patch_data.dict(exclude_unset=True)
            updated_user= stored_user_data.copy(update=update_data)
            user_db[user_db.index(user)] = updated_user
            return {"message" : f"book with id {user_id} has been patched", "book" : updated_user}
    if stored_user_data is None:
        raise HTTPException(status_code=404, detail=f"Book with id {user_id} not found")