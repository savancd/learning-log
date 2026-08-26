def get_formated_name(first_name, last_name):
	"""Return full name, formated"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()


while True:
	print("(Enter 'q' at any time to quit)")

	f_name = input(f"First name:").lower()
	if f_name == "q":
		break
	l_name = input(f"Last name:").lower()
	if l_name == "q":
		break

	formated_name = get_formated_name(f_name, l_name)
	print(f"\nHello, {formated_name}")
