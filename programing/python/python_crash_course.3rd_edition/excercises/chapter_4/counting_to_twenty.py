# counting to twenty-

# importing library for changing numbers to text
from num2words import num2words

# counting from 1 to 20
for n in range(1, 21):
	# changing numbers to  text and printing on the screen
	print(f"This is a number {num2words(n)}:  {n}")


