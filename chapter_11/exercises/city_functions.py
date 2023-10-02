def get_city_country_name(city, country, population=0):
    """Generates elegant formatted data about the country and city."""
    if population != 0:
        formatted_name = f'{city.title()}, {country.title()} - {population} population'
        return formatted_name
    else:
        formatted_name = f'{city}, {country}'
        return formatted_name.title()
