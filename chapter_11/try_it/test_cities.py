from city_functions import get_location_name

def test_city_country():
    formatted_location=get_location_name("Gampha","Sri Lanka")
    assert formatted_location == "Gampha, Sri Lanka"


def test_city_country_population():
    formatted_location = get_location_name("Gampha", "Sri Lanka",2000000)
    assert formatted_location == "Gampha, Sri Lanka - Population 2000000"
