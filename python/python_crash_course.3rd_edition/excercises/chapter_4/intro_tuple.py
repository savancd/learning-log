
# Buffet style restaurant offers only five basic foods.
# Five simple foods, store them i a tuple
# Use a for loop to print each food item
# Try to modify items
# The restaurant changes it's menu, replacing two of the items with a different foods
# Add a line that rewrite the tuple, and use for loop to print each item of the revised menu



def main():

	# Tuple of values
	foods = ("apple", "bread", "egg", "rice", "cheese")

	print("Original menu:\n")
	# enumerating original list and printing it to screen
	for n, food in enumerate(foods):
		n += 1 # starting from a 1 not a 0
		print(f"Item {n} is: {food.title()}.") # .title() making all first capital letter

	print(30 * "=")

	new_food_menu_tuple = ("apple", "bread", "egg", "banana", "fish")

	# enumerating new list and printing it to screen
	print("Revised menu:\n")
	for n, food in enumerate(new_food_menu_tuple):
		n += 1 # starting from a 1 not a 0
		print(f"Item {n} is: {food.title()}.") # .title() making all first capital letter




if __name__ == "__main__":
	main()

