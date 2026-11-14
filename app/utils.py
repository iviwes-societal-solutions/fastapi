import bcrypt

def hash(password: str):
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt()).decode()