



# def function
def fix_start(s): # with a string s
	if len(s) <= 1: # if the s is less or equal to 1 it's gonna return s
		return s


	first = s[0] # spliting first char of the word
	rest = s[1:] # spliting rest of characters of the word

	# rest_replaced will replace every letter character that is the same as a first characted that will stay the same
	rest_replaced = rest.replace(first, "*") # resplace rest with a character star
	# it's gonna combine them into one
	return first + rest_replaced


# def main
def main():
	# giving a value babble
	s = "babble"
	result = fix_start(s)
	print(result)




if __name__ == "__main__":
	main()
