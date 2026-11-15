from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class UserPrint(BaseModel):
    id: int
    email: EmailStr
    create_at: datetime

    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True

class PostsRespose(PostBase):
    create_at: datetime

class PostReponse(BaseModel):
    title: str
    content: str
    create_at: datetime

    class Config:
        from_attributes = True