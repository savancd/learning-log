

# dictionaries compared to a list must be with curly braces "{}"
alien = {"color": "green", "points": 5}

# deleting the key value pair
del alien["points"]
print(alien)



point_value = alien.get("points", "No value assigned")
print(point_value)
