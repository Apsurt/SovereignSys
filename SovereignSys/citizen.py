import os
import numpy as np
import datetime
from fastapi import status
from fastapi.responses import JSONResponse
from .app_builder import app
from .data_models import Citizen, Date

@app.post("/citizen/create")
async def create_citizen(citizen: Citizen, idx: int = 0):
    with open(f"SovereignSys/citizens/citizen{idx}.json", "w") as f: #CHANGE THIS WHEN MOVING TO DB
        f.write(citizen.model_dump_json(indent=2))
    return citizen

@app.post("/citizen/create_random")
async def create_random_citizens(n: int = 1):
    citizens = []
    for idx in range(n):
        citizen = random_citizen()
        with open(f"SovereignSys/citizens/citizen{idx}.json", "w") as f: #CHANGE THIS WHEN MOVING TO DB
            f.write(citizen.model_dump_json(indent=2))
        citizens.append(citizen)
    return citizens

@app.get("/citizen/get")
async def get_citizen(idx: int = None, pn: int = None):
    args = [idx, pn]
    argument_exists = False
    for arg in args:
        if not arg is None:
            argument_exists = True
            break
    if not argument_exists:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"response": "No arguments passed. Check docs."})
    
    path = f"SovereignSys/citizens"  #CHANGE THIS WHEN MOVING TO DB
    #find by idx
    if not idx is None:
        file_path = path + f"/citizen{idx}.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                citizen = Citizen.model_validate_json(f.read())
                return citizen
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"response": f"Citizen with index {idx} doesn't exist."})

    #find by personal number
    if not pn is None:
        for citizen_path in os.listdir(path): #CHANGE THIS WHEN MOVING TO DB
            with open(os.path.join(path, citizen_path), "r") as f:
                citizen = Citizen.model_validate_json(f.read())
            if int(citizen.personal_number) == pn:
                return citizen
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"response": f"Citizen with personal number {pn} doesn't exist."})
    
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"response": f"Something went wrong."})

def random_citizen():
    sex = "Male" if np.random.randint(0,2) == 0 else "Female"
    
    with open(f"SovereignSys/resources/{sex.lower()}_names.txt", "r") as f:
        name = np.random.choice(f.readlines()).strip().lower().capitalize()
    with open("SovereignSys/resources/surnames.txt", "r") as f:
        surname = np.random.choice(f.readlines()).strip().lower().capitalize()
    full_name = " ".join((name, surname))
    
    min_date = datetime.date(1930, 1, 1)
    today = datetime.date.today()
    birth_date = min_date + (today - min_date) * np.random.random()
    birth = Date(day=birth_date.day, month=birth_date.month, year=birth_date.year)
    
    with open("SovereignSys/resources/jobs.txt", "r") as f:
        job = np.random.choice(f.readlines()).strip()

    age = (today - birth_date).days / 365.25
    if age < 25:
        job = "University Student"
    if age < 19:
        job = "Student"
    if age < 7:
        job = "Child"
    
    #My idea of polish PESEL
    personal_number = ""
    personal_number += str(birth.year)[-2:].zfill(2)
    personal_number += str(birth.month).zfill(2)
    personal_number += str(birth.day).zfill(2)
    personal_number += str(1) if sex=="Male" else str(0)
    pn_hash = str(abs(hash(personal_number)))[:7]
    personal_number += pn_hash
    
    #ISO/IEC 7501-1 standard
    country_code = "XYZ" #TODO get country here
    passport_number = "P"
    passport_number += "<"
    passport_number += country_code
    passport_number += surname.upper()
    passport_number += "<<"
    passport_number += name.upper()
    passport_number += "<" * (44-len(passport_number))
    passport_number += "\n"
    
    unique_passport_number = ""
    for i in range(9):
        unique_passport_number += str(np.random.randint(0,10))
    passport_number += unique_passport_number
    passport_number += "0" #TODO Real checknumber
    passport_number += country_code
    passport_number += str(birth.year)[-2:].zfill(2)
    passport_number += str(birth.month).zfill(2)
    passport_number += str(birth.day).zfill(2)
    passport_number += "0" #TODO Real checknumber
    passport_number += sex[0]
    passport_number += str(today.year + 10)[-2:].zfill(2)
    passport_number += str(today.month).zfill(2)
    passport_number += str(today.day).zfill(2)
    passport_number += "0" #TODO Real checknumber
    passport_number += personal_number
    passport_number += "0" #TODO Real checknumber
    passport_number += "0" #TODO Real checknumber
    
    return Citizen(name=full_name, sex=sex, birth=birth, job=job, personal_number=personal_number, passport_number=passport_number)