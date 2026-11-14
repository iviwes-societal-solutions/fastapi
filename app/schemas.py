from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    second_name: str = None
    last_name: str
    id_number: str
    email: EmailStr
    cellphone: str
    password: str