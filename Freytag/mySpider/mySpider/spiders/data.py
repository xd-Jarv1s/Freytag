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
}

# Extract data based on patterns
extracted_data = {key: extract_and_format(specific_data, pattern) for key, pattern in patterns.items()}

# Combine and format the results
combined_results = extracted_data["dates"] + extracted_data["events"]

# Output the combined results and the link
print(specific_data)
