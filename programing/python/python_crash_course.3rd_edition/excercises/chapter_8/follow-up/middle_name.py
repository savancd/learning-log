# To make get_formatted_name() work without a middle name, we set the
# default value of middle_name to an empty string and move it to the end of the
# list of parameters:

def formated_name(first_name, last_name, middle_name=""):
	"""Returns full name,formated"""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = formated_name("jimi", "hendrix")
print(musician)


musician = formated_name("john", "hooker", "lee")
print(musician)


# the name is built from three possible parts. Because
# there’s always a first and last name, these parameters are listed first in the
# function’s definition. The middle name is optional, so it’s listed last in the
# definition, and its default value is an empty string.
