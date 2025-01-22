import requests
from bs4 import BeautifulSoup

url = 'https://suryanshsk.pro/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting all headings from the page
headings = soup.find_all('h2')
for heading in headings:
    print(heading.text)
