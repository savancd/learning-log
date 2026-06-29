# setting up dictionary
favorite = {
	"jen": "python",
	"sarah": "c",
	"edward": "rust",
	"phil": "python",
	}

# making a list
friends = ["phil", "sarah"]

print(type(favorite))
print("=" * 30)

# loopng through keys and value in favorite dict
for name, value in favorite.items():
	print(f"{name.title()} loves to code in {value.upper()}")

	if name in friends:
		language = favorite[name].title()
		# the \t means that will be indented
		print(f"\t{name.title()}, I see you love {language}")

# can be targeted just the values in a dict
for language in favorite.values():
	print(language.title())



languages = {"python", "rest", "python", "c"}

print(languages)
