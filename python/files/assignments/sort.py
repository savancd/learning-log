#   This is made for the assignments to create a module with at least three functions 
#   that perform different tasks, such as sorting a list].

movies = [
	(1994, 'The Shawshank Redemption', 9.2),
	(1999, 'Fight Club', 8.8),
	(1994, 'Pulp Fiction', 8.9),
	(1972, 'The Godfather', 9.2),
	(2008, 'The Dark Knight', 9.0)
]

movies = sorted(movies, key=lambda movie: movie[0])

for movie in movies:
     print(movie)

# 	Resources for making this function was: 
# 	https://blogboard.io/blog/knowledge/python-sorted-lambda/
#	https://docs.python.org/3/howto/sorting.html

