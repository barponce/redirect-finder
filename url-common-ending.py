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
    common_ending = None
    for part in url_parts[::-1]:
        if part:
            common_ending = part
            break
    if common_ending is not None:
        if common_ending not in url_endings:
            url_endings[common_ending] = []
        url_endings[common_ending].append(entry)

# Output the URLs with the same common ending
for url_ending, entries in url_endings.items():
    if len(entries) > 1:  # Check if there are multiple entries for the URL ending
        print("URLs with common ending:", url_ending)
        for entry in entries:
            print(entry["url"])
        print()
