
# Defining the function
# None is a placeholder value, which is used when variable is not having specific value assigned to it
def build_person(first_name, last_name, age=None):
	"""Return a dictionary of information about a person"""
	person = {"first": first_name, "last": last_name}
	# if there is a age its gonna print it, even if there is no age its gonna print the name and last name
	if age:
		person["age"] = age
	return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)
