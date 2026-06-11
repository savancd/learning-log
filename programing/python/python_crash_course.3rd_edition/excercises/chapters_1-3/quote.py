
# Famous quote Python Challenge


# Welcome message to user
print("Welcome to this app! ")


user = input("Please Enter Your favorite quote from some famous person:\n")
# striping the empty spaces at the beginning and end
user_text = user.strip()
# making text short if the user  enter too long text
short = user_text[:250]
short_cap = short.capitalize()

# author
author_list  = []


#print(type(author_list))


if user == "":
	print('"No quote provided" -- unknown')
else:
	print("Who is the author of the quote?")
	author_imp = input("Please give us Author of the quote:\n")
	author_list.append(author_imp)


for author in author_list:
	author_cap = author.title()
	print()
	print(f'You Entered:\n"{short_cap}"\n \u2014 {author_cap}')

