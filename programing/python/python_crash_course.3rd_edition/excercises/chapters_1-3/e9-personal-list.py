

# Personal list
# Make a personal list of a vehicle favorite one. And make print statement about these vehicles.


# List of cars and bikes
cars =  ["ferary", "honda", "toyota"]
bikes = ["ducati", "yamaha"]

# Custom message when printing
message = "I would like to own a "

# Examples what would like to have
car = "ferary"
bike = "ducati"

# Empty list
lista = []



if car in cars:
	lista.append(car)

if bike in bikes:
	lista.append(bike)

print(f"{message}{lista[0].title()} and a {lista[1].title()}.")

additional_message = "Actually I would like as well to own "
#lista[1] = "two ducati's"

#print(f"{additional_message}{lista[0].title()} and {lista[1].title()}")


# Inserting new value/item in the list
lista.insert(2, "harley davidson")

print(f"{additional_message} {lista[2].title()}")
