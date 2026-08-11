
def describe_city(city, country="Iceland"):
	"""print a simple sentence"""
	print(f"{city.title()} is in the {country}")

describe_city("Reykjavik")
describe_city("Paris", "France")
