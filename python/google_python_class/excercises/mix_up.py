

# defining function with a string a, b
def mix_up(a, b):
	# spliting first character in a word
	a_split = a[:1]
	b_split =  b[:1]
	# spliting rest of characters from a word so it can be combined
	a_rest = a[1:]
	b_rest = b[1:]
	# mixing first splited character with a rest of characters from another word
	a_mix = b_split + a_rest
	b_mix = a_split + b_rest

	# must have return value
	return a_mix + " " + b_mix # return value mixed words

def main():
	# creating variables with a values that are going to be mixed
	a = "dog"
	b = "dinner"

	result = mix_up(a, b)
	print(result)






if __name__ == "__main__":
	main()
