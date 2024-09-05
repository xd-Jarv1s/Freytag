import json
import re

# Load the JSON file
with open('dataClean.json', 'r') as file:
    data = json.load(file)

# Access the specific data
specific_data = data[0]["data"][15]

print(specific_data)
