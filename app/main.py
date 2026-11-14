from fastapi import FastAPI, status, HTTPException, Depends
from typing import List
from .database import get_db, engine
from . import models, schemas, utils
from sqlalchemy.orm import Session

def cls():
    system("cls")

app = FastAPI()

@app.get("/api/health")
def health():
    return {
        "health": "OK"
    }


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Users not found')
    return users

@app.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Could not find user with id {}'.format(id))
    return user

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password) # Exctract and hash passwd
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        new_user
    }

if __name__ == "__main__":
    system("python -m uvicorn main:app --reload --port 8089")