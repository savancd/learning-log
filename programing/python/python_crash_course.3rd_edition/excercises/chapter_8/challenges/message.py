# Write a function calld display_message() that prints one sentence telling everyone that you are 
# learning this chapter 8, call the function and make sure message displays correctly


def display_message():
	print('I am learning Functions in Chapter 8 of the book "Automating_with_Python_3rd"')

def favorite_book(title):
	"""This function should print a message"""
	print(f"One of my favorite books is: {title.title()}!")


display_message()
favorite_book("alice in wonderland")
