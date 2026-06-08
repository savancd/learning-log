# Slices

# Print the message "The first three items in the list are" 
# The use the slice to print three items from the middle of the list

# Print the message "The items from the middle of the list are"
# Then use the slice to print those three items from the middle of the list

# Print the message "The last three items in the list are"
# Then use a slice to print the last three items in the list



# food list
foods = ["pizza", "falafel", "carrot cake", "cannoli", "ice cream"]

# counting how many food items there is in the list
print(len(foods))

# slicing lists from a list foods
foods_first_three = foods[:3]
foods_middle_three = foods[2:]
foods_last_three = foods[-3:]

# Printing all messages with a .join to remove all brackets ...
print(f"The first three items in the list are:  {', '.join(foods_first_three)}")
print(f"The items from the middle of the list are:  {', '.join(foods_middle_three)}")
print(f"The last three items in the list are:  {', '.join(foods_last_three)}")
