import json

# Example JSON data
with open('data.json') as f:
    json_data = f.read()

json_obj = json.loads(json_data)
url_endings = {}

# Group entries by URL ending
for entry in json_obj:
    url = entry["url"]
    url_parts = url.split("/")
    url_ending = url_parts[-1] if url_parts[-1] else url_parts[-2]
    if url_ending not in url_endings:
        url_endings[url_ending] = []
    url_endings[url_ending].append(entry)

# Find entries with the same URL ending
matching_entries = []
for url_ending, entries in url_endings.items():
    if len(entries) > 1:  # Check if there are multiple entries for the URL ending
        matching_entries.extend(entries)

# Output the matching entries
for entry in matching_entries:
    print("Matching Entry:")
    print("URL:", entry["url"])
    print()


