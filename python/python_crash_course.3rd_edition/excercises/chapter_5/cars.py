

# Print all cars in title() except bmw that should be printed all in uppercase

cars = [
    "toyota", "honda", "ford", "bmw", "tesla", "chevrolet", "nissan", "hyundai",
    "kia", "volkswagen", "mercedes", "audi", "lexus", "subaru", "mazda", "mitsubishi",
    "jaguar", "land rover", "peugeot", "renault", "volvo", "skoda", "infiniti", "mini"
]


for n, car in enumerate(cars):
	n += 1
	cars.sort()
	if car == "bmw":
		print(f"{n}: {car.upper()}")
	else:
		print(f"{n}: {car.title()}")

