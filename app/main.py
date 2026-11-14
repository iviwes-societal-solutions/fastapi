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

@app.get("/users/{id}")
def get_user(id: int):
    try:
        conn = psql.connect(DB_URL)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""SELECT * FROM users WHERE id = %s""", (id,))
        user = cur.fetchone()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Coudln't find user with id {id}")
        return user
    finally:
        conn.close()

@app.post("/users")
def create_user(user: UserCreate):
    pass

if __name__ == "__main__":
    system("python -m uvicorn main:app --reload --port 8089")