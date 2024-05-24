import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get("https://example.com")
r.content

# Parse the HTML content
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the data you want
data = soup.find_all('div', class_='example-class')

# Store the data in a text file
with open('output.txt', 'w') as f:
    for item in data:
        f.write(item.get_text() + '\n')
