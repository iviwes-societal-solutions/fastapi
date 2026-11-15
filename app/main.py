from fastapi import FastAPI, status, HTTPException, Depends
from typing import List
from .database import get_db, engine
from . import models, schemas, utils
from sqlalchemy.orm import Session
import os

models.Base.metadata.create_all(bind=engine)

def cls():
    os.system("cls")

app = FastAPI()

@app.get("/api/health")
def health():
    return {
        "health": "OK"
    }


@app.get("/users", response_model=List[schemas.UserPrint])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Users not found')
    return users

@app.get("/users/{id}", response_model=schemas.UserPrint)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Could not find user with id {}'.format(id))
    return user

@app.put("/users/{id}", response_model=schemas.UserPrint, status_code=201)
def update_user(id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    cls()
    user.password = utils.hash(user.password)
    user_query = db.query(models.User).filter(models.User.id == id)
    if not user_query.first():
        raise HTTPException(status_code=404, detail=f"User with id {id} is not found")
    user_query.update(user.model_dump())
    db.commit()
    db.refresh(user_query.first())
    return user_query.first()

@app.post("/users", status_code=status.HTTP_201_CREATED)#, response_model=schemas.UserPrint)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password) # Exctract and hash passwd
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        new_user
    }

@app.delete("/users/{id}", status_code=204)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=404, detail=f'No user with id {id}')
    user.delete(synchronize_session=False)
    db.commit()

@app.get("/posts", response_model=List[schemas.PostsRespose])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts")
    return posts

@app.get("/posts/{id}", response_model=schemas.PostReponse)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Couldn't find post with id {id}")
    return post

@app.put("/posts/{id}", response_model=schemas.PostReponse, status_code=201)
def update_post(id: int, post: schemas.PostBase, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    if not post_query.first():
        raise  HTTPException(status_code=404, detail=f"No post with id {id}")
    post_query.update(post.model_dump())
    db.commit()
    db.refresh(post_query.first())
    return post_query.first()

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.PostsRespose)
def create_post(post: schemas.PostBase, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=404, detail=f'No post with id {id}')
    post.delete(synchronize_session=False)
    db.commit()

if __name__ == "__main__":
    os.system("python -m uvicorn main:app --reload --port 8089")