from fastapi import FastAPI, status, HTTPException
from os import system
import dotenv
from pydantic import BaseModel, EmailStr
from datetime import datetime
from psycopg2.extras import RealDictCursor
import psycopg2 as psql
from typing import List, Optional

# INSERT INTO users(first_name, second_name, last_name, id_number, email, cellphone, password)

class UserCreate(BaseModel):
    first_name: str
    second_name: str = None
    last_name: str
    id_number: str
    email: EmailStr
    cellphone: str
    password: str

def cls():
    system("cls")


env = dotenv.find_dotenv()

DB_URL = dotenv.get_key(key_to_get="DB_URL", dotenv_path=env)

app = FastAPI()

@app.get("/api/health")
def health():
    try:
        conn = psql.connect(DB_URL)
        cur = conn.cursor()

    except Exception as e:
        print(e)

    finally:
        if conn:
            print("Closing connection")
            conn.close()
    name = "Mshengu Lunika"
    print(name)
    return {
        "name": name
    }

@app.get("/")
def function():
    try:
        conn = psql.connect(DB_URL)
        cur = conn.cursor()

    except Exception as e:
        print(e)

    finally:
        if conn:
            print("Closing connection")
            conn.close()
    return {
        "message": "index page"
    }

@app.get("/users")
def get_users():
    cls()
    try:
        conn = psql.connect(DB_URL)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        print(users)
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Couldn't retrieve users")
        return users

    finally:
        if conn:
            print("Closing connection")
            conn.close()

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
    try:
        conn = psql.connect(DB_URL)
        cur = conn.cursor(cursor_factory=RealDictCursor)

    finally:
        conn.close()

if __name__ == "__main__":
    system("python -m uvicorn main:app --reload --port 8089")