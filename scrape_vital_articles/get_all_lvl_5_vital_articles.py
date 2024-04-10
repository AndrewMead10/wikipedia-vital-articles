import requests
from bs4 import BeautifulSoup

base_url = "https://en.wikipedia.org"

with open("links.txt", "r") as f:
    links = f.readlines()

links = [base_url + link.strip() for link in links]


for link in links:

    response = requests.get(link)

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="wikitable")

    # Find the target div by its ID
    div = soup.find("div", id="Wikipedia_core_topic_lists")

    # Initialize an empty list to store the filtered href values
    filtered_links = []

    # Ensure both the table and div are found
    if table and div:
        print("Table and div found!")
        # Extract all <a> tags between the table and the div
        passed_table = False
        for tag in table.find_next_siblings():
            if tag == div:
                break  # Stop if we've reached the div
            if tag.name == "a" and not (
                "Edit" in tag.get("title", "")
                or "Level" in tag.get("title", "")
                or "File" in tag.get("href", "")
            ):
                # Append the href value if it doesn't contain 'Edit' or 'Level' in the title
                filtered_links.append(tag["href"])
            # Also look for <a> tags inside other container elements between the table and div
            elif tag.find_all("a"):
                for a in tag.find_all("a"):
                    if not (
                        "Edit" in a.get("title", "")
                        or "Level" in a.get("title", "")
                        or "File" in a.get("href", "")
                    ):
                        if a["href"] == "/wiki/Template:Core_topics":
                            break
                        filtered_links.append(a["href"])

    # append the links to a file
    with open("vital_article_links.txt", "a") as f:
        for link in filtered_links:
            f.write(link + "\n")
