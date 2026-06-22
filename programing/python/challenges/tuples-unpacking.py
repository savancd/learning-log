# learning challenge

# create two variables with different values
# print both variables
# swap their values using tuple unpacking
# print values afain to verify the swap
# unpack tuple into separate variable
# print it



house_location = "miami"
property_type = "condominium"

print(f"The house is on in the {house_location.title()} and the property is {property_type.title()}")

# tuple with multiple values
real_estate = ("miami", "jon doe", "condominium", 1_000_000)

# unpacking the tuple into variable names
# the names must align with a number of values
city, buyer, property, price = real_estate

# Now it can print separately by targeting a name
print(city)

# other way to print all from a list
for i, n in enumerate(real_estate):
	i += 1
	print(i, n)

value1, value2 = "miami",  1_000_000

print(f"value1: {value1}")
print(f"value2: {value2}")

# swaping values
value1, value2 = value2, value1

print("value1:", value1)
print("value2:", value2)
