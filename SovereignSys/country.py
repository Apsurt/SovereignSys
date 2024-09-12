import os

from fastapi import status
from fastapi.responses import JSONResponse
from .app_builder import app
from .data_models import Country

@app.post("/country/create")
async def create_country(country: Country, idx: int = 0):
    with open(f"SovereignSys/countries/country{idx}.json", "w") as f:
        f.write(country.model_dump_json(indent=2))
    return country

@app.get("/country/get")
async def get_country(idx: int = 0):
    path = f"SovereignSys/countries/country{idx}.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            country = Country.model_validate_json(f.read())
        return country
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"response": f"Country with index {idx} doesn't exist."})