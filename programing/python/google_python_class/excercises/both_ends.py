


# First define a function both_ends
def both_ends(s):
	# if s is less then 2 then do
	# calculate amount of characters with a len()
	if len(s) < 2: # if less then 2
		# return the empty string
		return ""
	# if not less then 2  then split first teo and last char
	return s[:2] + s[-2:] 



# Fuction def should be out of the main


# Define main
def main():
	# take the string s from a def function
	# and give it a value
	s = "yields"
	# place it in new 
	result = both_ends(s) # call the def function with a string name
	# print it to the screen
	print(result)



if __name__ == "__main__":
	main()

