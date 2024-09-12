from pydantic import BaseModel
from datetime import date
from typing import List

class Citizen(BaseModel):
    name: str
    sex: str
    birth: date
    personal_number: int
    passport_number: int

class Country(BaseModel):
    name: str
    citizens: List[Citizen]