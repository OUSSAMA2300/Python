def describe_city(city_name, country='egypt'):
    print(city_name.title(), "is in", country.title())

# Using the default
describe_city('cairo')

describe_city('alex')

describe_city('reykjavik', 'iceland')