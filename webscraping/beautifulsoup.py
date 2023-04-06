from bs4 import BeautifulSoup as BS
import requests

try:
    url = 'https://www.jumia.com.ng/phones-tablets/'
    response = requests.get(url).text
except Exception as e:
    print(e.args)

contents = BS(response, 'html.parser')
# print(contents.prettify())

# sections = contents.find_all('div', class_='-phxs')[1]
# items = sections.find_all('div', class_='itm')

# for item in items:
#     print()
    # name = item.find('div', class_='name')
#     print(name.text)
#     price = item.find('div', class_='prc')
#     print(price.text)

sections = contents.find('div', class_ ='-paxs')
items = sections.find_all('article', class_='prd')
# print(items)


for item in items:
    print()
    name = item.find('h3', class_='name')
    print(name.text)
    price = item.find('div', class_='prc')
    print(price.text)

# with open('sample2.html', 'r') as f:
#     doc = BeautifulSoup(f, 'html.parser')

# # print(doc.prettify())
# first_paragraph1 = doc.find('p')

# print(first_paragraph1.text)