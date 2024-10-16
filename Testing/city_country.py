def city_functions(city, country, population=''):
    """Describe a city"""
    if population:
        city_country = f"{city}, {country} -Population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()