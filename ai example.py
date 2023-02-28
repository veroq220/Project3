import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

style_tags = soup.find_all('style')
for tag in style_tags:
    bg_color = tag.get('background-color: ')
    print(bg_color)
