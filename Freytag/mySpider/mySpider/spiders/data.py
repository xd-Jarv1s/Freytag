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

# Define regex patterns
patterns = {
    "dates": r'"Datum":"(\d{2}\.\d{2}\.\d{4})"',
    "events": r'"category":"([a-zA-Z\s]+)"',
    "time_starts": r'"timeStart":"(\d{2}:\d{2})"',
    "time_ends": r'"timeEnd":"(\d{2}:\d{2})"',
    "subtitles": r'"subtitle":"([^"]+)"',
    "label": r'"label":"([^"]+)"',
    "value": r'"value":"([^"]+)"',
    "category": r'"category":"([^"]+)"',
}

# Extract data based on patterns
extracted_data = {key: extract_and_format(specific_data, pattern) for key, pattern in patterns.items()}

# Create a link using extracted 'wo' and 'was'
wo_value = extracted_data.get("location")[0] if extracted_data.get("location") else ''
was_value = extracted_data.get("events")[0] if extracted_data.get("events") else ''
base_url = "https://frey-tag.at/"
full_url = f"{base_url}/kalender?page=1&wo={wo_value}&was={was_value}"

# Combine and format the results
combined_results = extracted_data["dates"] + extracted_data["events"] + extracted_data["time_starts"] + extracted_data["time_ends"] + extracted_data["subtitles"] + extracted_data["date_start"]

# Output the combined results and the link
print(combined_results)
print(full_url)
