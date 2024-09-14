import requests
import json
from SovereignSys import Citizen, Date

def test_create_single_random_citizen():
    response = requests.post("http://127.0.0.1:8000/citizen/create_random/", timeout=2)
    print(response.text)
    assert response.status_code == 200
    citizen = Citizen.model_validate(response.json()[0])
    assert citizen.name is not None
    assert citizen.personal_number is not None

def test_create_multiple_random_citizens():
    response = requests.post("http://127.0.0.1:8000/citizen/create_random/?n=10", timeout=10)
    print(response.text)
    assert response.status_code == 200
    citizens = [Citizen.model_validate(c) for c in response.json()]
    assert len(citizens) == 10
    for citizen in citizens:
        assert citizen.name is not None
        assert citizen.personal_number is not None

def test_get_citizen_by_index():
    create_response = requests.post("http://127.0.0.1:8000/citizen/create_random/", timeout=2)
    created_citizen = Citizen.model_validate(create_response.json()[0])

    response = requests.get(f"http://127.0.0.1:8000/citizen/get?idx=0", timeout=2)
    print(response.text)
    assert response.status_code == 200
    retrieved_citizen = Citizen.model_validate_json(response.text)
    assert retrieved_citizen.personal_number == created_citizen.personal_number

def test_get_citizen_by_personal_number():
    create_response = requests.post("http://127.0.0.1:8000/citizen/create_random", timeout=2)
    created_citizen = Citizen.model_validate(create_response.json()[0])

    response = requests.get(f"http://127.0.0.1:8000/citizen/get?pn={created_citizen.personal_number}", timeout=2)
    print(response.text)
    assert response.status_code == 200
    retrieved_citizen = Citizen.model_validate_json(response.text)
    assert retrieved_citizen.personal_number == created_citizen.personal_number

