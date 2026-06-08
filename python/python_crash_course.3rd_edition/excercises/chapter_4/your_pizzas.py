
# My Pizzas and Your Pizzas

# Make a copy of the list of pizzas, and call it friend_pizzas.
# Add a new pizza to the original list
# Add different pizza to the friend list
# Prove that those lists are different. Print a message 
# My favorite pizzas are:  and use a loop to print a second list


# define main
def main():
	# Original list 
	pizza_list = ["peperoni", "capricosa", "vojvodjanka"]
	# The second list  that is copy from original one
	friend_pizzas = pizza_list[:]


	pizza_list.append("margarita")
	friend_pizzas.append("quatro stagione")

	for n, pizza in enumerate(pizza_list):
		n += 1
		print(f"{n}: One of my favorite pizza is {pizza}")

	print(40 * "=")

	for n, pizza in enumerate(friend_pizzas):
		n += 1
		print(f"{n}: My friend loves pizza  {pizza}")




if __name__ == "__main__":
	main()
