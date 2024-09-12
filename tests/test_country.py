import requests
from SovereignSys import Country, Citizen, Date
from datetime import date

def test_create_country():
    citizen = Citizen(name="Cookie Monster", sex="Male", birth=Date(year=1969, month=11, day=10), personal_number=0, passport_number=0)
    country = Country(name="Sesame Street", citizens=[citizen])
    
    response = requests.post("http://127.0.0.1:8000/country/create", json=country.model_dump(), timeout=1)
    
    print(response.text)
    assert response.status_code == 200

def test_get_country():
    response = requests.get("http://127.0.0.1:8000/country/get")
    print(response.text)
    assert response.status_code == 200
    country = Country.model_validate_json(response.text)
    assert country.name == "Sesame Street"