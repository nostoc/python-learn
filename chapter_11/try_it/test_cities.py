from city_functions import get_location_name

def test_city_country():
    formatted_location=get_location_name("Gampha","Sri Lanka")
    assert formatted_location == "Gampha, Sri Lanka"