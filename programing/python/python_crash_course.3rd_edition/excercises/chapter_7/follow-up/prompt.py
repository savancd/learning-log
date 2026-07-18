# This example shows how to build multiline string

# this line assigns the 
prompt = "If you share your name, we can personalize the messages you see"
prompt += "\nWhat is your first name?  "


name = input(prompt)
print(f"\nHello, {name}!")
