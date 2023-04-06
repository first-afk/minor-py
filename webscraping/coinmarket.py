from bs4 import BeautifulSoup
import requests

try:
    url = 'https://coinmarketcap.com/'
    response = requests.get(url).text
except Exception as e:
    print(e.args)

contents = BeautifulSoup(response, 'html.parser')

section = contents.find('table', class_='ieTeVa')
items = section.find('tbody')
body = items.find_all('tr')


for item in body[0:10]:
    print()
    div = item.find('div', class_='iATetF')
    name = div.find('p', class_='kKpPOn')
    print(name.text)

    a = item.find('div', class_='enIhIB')
    span = a.find('a', class_='cmc-link')
    price = span.find('span')
    print(price.text)

    meta = item.find('span', class_='bQjSqS')
    print(meta.text)