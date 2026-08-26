# Write a function that takes in the name of a city and its country.


def city_country(name, country):
	city = {"name": name, "country": country}
	return city

city_1 = city_country("Tokyo", "Japan")
city_2 = city_country("Paris", "France")
city_3 = city_country("Cairo", "Egypt")

print(f"City 1: {city_1['name']}, {city_1['country']}\nCity 2: {city_2['name']}, {city_2['country']}\nCity 3: {city_3['name']}, {city_3['country']}")
