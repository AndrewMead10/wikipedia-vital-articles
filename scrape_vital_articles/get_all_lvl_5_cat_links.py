import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/5"

# Send a GET request to the page
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find the table by its class
table = soup.find("table", class_="wikitable")

print(table)

# Initialize an empty list to store the links
links = []

# Check if the table was found
if table:
    print("Table found!")
    # Find all <a> tags within the table
    for a in table.find_all("a", href=True):
        # Append the href attribute (URL) of each <a> tag to the links list
        links.append(a["href"])

# save links to a file
with open("links.txt", "w") as f:
    for link in links:
        f.write(link + "\n")
