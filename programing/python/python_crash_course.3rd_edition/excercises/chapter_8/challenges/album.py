# write a function  that builds a dictionary describing a music album. The function should
# take an artist name and album title, it should return a dictionary containing these two 
# pieces of information

# This is creating a string
"""
def make_album(name, album_name, songs=None):
	album_make = f"{name} {album_name}"
	if songs:
		album_make["songs"] = songs
	return album_make
"""

# this one create a dict of the name and title
def make_album(name, album_name, songs=None):
	return {
		"name": name,
		"album": album_name,
		"songs": songs
	}

album = make_album("michael jackson", "thriller", 6)
print(type(album))
print(album)

print("#" * 40)

for k, n in album.items():
	if isinstance(n, (int, float)):
		print(n)
	else:
		print(f"{n.title()}")

print("#" * 40)

name = album["name"]
title = album["album"]
songs = album["songs"]

print(f"The name is: {name}\nTitle of the album is:  {title}\nNumber of songs: {songs}")

print("#" * 40)
print("#" * 40)

# creating empty dict
album_dict = {}
# numbering every new entry
num = 1


# adding new input into dict
while True:
	name = input("Please Enter a name:\n\t")
	title = input("Please Enter a title:\n\t")
	songs = int(input("How many songs there is in album:\n\t"))

	user_inp = input(f'Do you want to enter more?\nPress "y" to continue or  "q" to quit\n#: ').lower()

	# creating dictionary
	album_dict[num] = {
		"name": name,
		"title": title,
		"songs": songs
	}

	# increasing num for one every time
	num += 1

	if user_inp == "y":
		continue
	elif user_inp == "q":
		break

for k, n in album_dict.items():
	print(k, n)






