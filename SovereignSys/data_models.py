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
    job: str
    personal_number: str
    passport_number: str

class Country(BaseModel):
    name: str
    citizens: List[Citizen]