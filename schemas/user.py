from typing import Optional
from pydantic import BaseModel # Es una manera de modelar los datos o crear tipos de datos

# Tipo de dato User basado en el modelo base
class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str