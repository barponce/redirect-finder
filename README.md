# redirect-finder
This is how you can analyze a dataset in JSON format and identify URLs with common endings, which may indicate potential SEO redirections. This Tool made me able to find potential url redirections, duplicated content and thin content optimisation opportunities in a site 
with more than 1 million urls. 

To begin the analysis, the code reads the JSON data from a file and loads it into a JSON object. This object represents the dataset, which contains URLs and associated information.

The code then initializes an empty dictionary called url_endings to store the URLs grouped by their common endings.

Next, the code iterates over each entry in the JSON object. For each entry, it retrieves the URL and splits it into different parts using the forward slash ("/") as a separator. 

Starting from the end of the URL, the code iterates backward through the URL parts until it finds a non-empty part, which represents the common ending of the URL.

Once the common ending is identified, the code checks if it already exists as a key in the url_endings dictionary. If the common ending is not present, a new key is created, and an empty list is associated with it. 

The entry is then appended to the list corresponding to its common ending.

After grouping the URLs by their endings, the code proceeds to output the URLs with the same common ending. It iterates over the url_endings dictionary and checks if there are multiple entries associated with a particular ending. 

If there are, it prints a message indicating the common ending and then iterates over the entries, printing each URL.

By executing this code, you can identify URLs with common endings, which may suggest potential SEO redirections. 

This information can be valuable for SEO professionals and website administrators, as it allows them to review and optimize the website structure to ensure better search engine visibility and user experience.


The JSON file to extract the data looked like this:


```javascript
[
    {"url": "https://www.example.com/page1"},
    {"url": "https://www.example.com/page2"},
    {"url": "https://www.example.com/page3"},
    {"url": "https://www.example.com/page4"},
    {"url": "https://www.example.com/page5"},
    {"url": "https://www.example.com/page6"},
    {"url": "https://www.example.com/page7"},
    {"url": "https://www.example.com/page8"},
    {"url": "https://www.example.com/page9"},
    {"url": "https://www.example.com/page10"}
]

```
