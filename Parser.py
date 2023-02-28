import requests
from bs4 import BeautifulSoup
import re

# Получаем HTML-страницу
url = 'https://www.example.com'
response = requests.get(url)
html = response.content

# Создаем объект BeautifulSoup и находим нужные элементы
soup = BeautifulSoup(html, 'html.parser')
title = soup.title.string
style = soup.style.string
links = soup.find_all('a')

# Выводим результаты
print('Заголовок страницы:', title)
print('Цвет страницы:', style)
print('Ссылки на странице: ')
for link in links:
    print(link.get('href'))
