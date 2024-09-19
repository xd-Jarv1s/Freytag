import json
import re

# Function to extract specific patterns from text
def extract_and_format(text, pattern):
    matches = re.findall(pattern, text)
    return [match for match in matches]

# Load the JSON file
with open('dataClean.json', 'r') as file:
    data = json.load(file)

# Access the specific data
specific_data = data[0]["data"][15]

slug = []
id = []

#NOTES

#--location

# Define regex patterns
date_pattern = r'"Datum":"(\d{2}\.\d{2}\.\d{4})"'
slug_pattern = r'"slug":"([^"]+)"'
id_pattern = r'"_id":"([^"]+)"'

# Extract data based on patterns
dates = extract_and_format(specific_data, date_pattern)
slugs = extract_and_format(specific_data, slug_pattern)
ids = extract_and_format(specific_data, id_pattern)

# For demonstration purposes, we will take the first match of each
if slugs and ids:
    slug = slugs[0]
    id = ids[0]

# Construct the output URL
link = f"https://frey-tag.at/kalender/{slug}?s={id}"

for _ in range(1):
    print(f"SLUG: {slug} | ID: {id}")

# Print the combined results and the link
print(dates)
print(link)