def get_location_name(city, country,population=""):
    if population:
        formatted_location_name = f"{city}, {country} - population {population}"
    else:
        formatted_location_name = f"{city}, {country}"

    return formatted_location_name.title()
