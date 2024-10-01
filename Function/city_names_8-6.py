def city_country(city_name, country):
    """City information"""
    formatted_country = city_name + ', ' + country 
    return formatted_country.title()

info = city_country('santiago', 'chile')
print(info)

info = city_country('cairo', 'egypt')
print(info)

info = city_country('france', 'paris')
print(info)