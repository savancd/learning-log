# This is a simple funtion name greet_user.py


# to create a function it should be done with "def name()"

def greet_user():
	"""Display simple greeting"""
	print("Hello!")


# to call the function
greet_user()


def greet_user2(username):
	"""DIsplay a simple greeting and the input during call of the script"""
	print(f"Hello, {username.title()}!")

greet_user2("MIke")
