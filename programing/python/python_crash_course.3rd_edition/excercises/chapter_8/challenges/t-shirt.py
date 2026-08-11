# write a function  that accepts a size and text of a message that should be printed on the shirt.
# The function  should print a sentence summarizing the sizze of the shirt and the message printed on it
# call the function a second time using keyword arguments


def make_shirt(size, message):
	"""Taking the size and message and printing it"""
	print(f"This is the size {size}")
	print(f"This is a message {message}")
	print("=" * 20)
	print(f"The size of shirt is {'Large'}")
	print(f"The message on the shirt is {'Some random message'}")

make_shirt("S", "Love Python")
make_shirt(size='"M"', message='"Today is a beautiful day!"')


