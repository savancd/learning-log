
def formated_name(first_name, last_name):
	"""Return a full name, formated"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()


musician = formated_name("jimi", "hendrix")
print(musician)
