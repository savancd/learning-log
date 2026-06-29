# importing module
import json

# importing the file
with open("files/glossary.json", "r", encoding="utf-8") as f:
	data = json.load(f)

print(f"The type of data file is: {type(data)} \n\nThe data of the file is:\n{data}")

print("=" * 30)

for n in data["glossary"]:
	print(f'The Python word: "{n["name"]}" and the value: "{n["value"]}"')
