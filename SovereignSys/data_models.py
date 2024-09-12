from pydantic import BaseModel
from typing import List

class Date(BaseModel):
    day: int
    month: int
    year: int

class Citizen(BaseModel):
    name: str
    sex: str
    birth: Date
    personal_number: int
    passport_number: int

class Country(BaseModel):
    name: str
    citizens: List[Citizen]