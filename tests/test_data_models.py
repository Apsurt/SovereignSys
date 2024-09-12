from SovereignSys import Country, Citizen, Date, country

date = Date(year=2001, month=5, day=18)
citizen = Citizen(name="Shrek", sex="Male", birth=date, personal_number=0, passport_number=0)
country = Country(name="Swamp", citizens=[citizen])

def test_Date():
    assert date.year == 2001
    assert date.month == 5
    assert date.day == 18

def test_Citizen():
    assert citizen.name == "Shrek"
    assert citizen.sex == "Male"
    assert citizen.birth == date
    assert citizen.personal_number == 0
    assert citizen.passport_number == 0

def test_Country():
    assert country.name == "Swamp"
    assert country.citizens == [citizen]