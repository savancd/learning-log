
# Conditional tests to write  and print a statement describing each test and the prediction for the results 
# of each test.

# importing library
import json


# importing the file with name movie names
with open("files/movie_list.json", "r") as file:
	data = json.load(file)

name = "Games Of Thrones"

if name == data["movies"]:
	print(f'There is "{name}" in movie list!')
	# printing all the movies in the list
else:
	print(f'There is no "{name}" in the movie list!')

print(30 * "=")

for n, movie in enumerate(data["movies"]):
	n += 1
	# printing by the id title of the movie
	print(n, movie["title"])
