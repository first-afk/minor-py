from bs4 import BeautifulSoup
import requests



# try:
#     # url = 'https://sunnewsonline.com/category/national/'
#     url = 'https://sunnewsonline.com/category/business/'
#     response = requests.get(url).text
# except Exception:
#     print('could not grt html contents') 

# web_html = BeautifulSoup(response, 'html.parser')
# section = web_html.find('content', class_='category-page')
# item = section.find_all('div', class_='row')[1]
# item = item.find('div', class_='row')

# data = item.find_all('a')

# for a in data:
#     print()
#     title = a.find('h3')
#     print(title.text)
#     print(a['href'])

# konga web scraping

try:
    url = 'https://www.konga.com/category/accessories-computing-5227'
    response = requests.get(url).text
except Exception as e:
    print(e.args)

sections = BeautifulSoup(response, 'html.parser')
contents = sections.find('section')
# print(contents.prettify)
mid_section = contents.find('div', class_='_9379b_2V_9s')
print(mid_section)
mid_content = mid_section.find('div', class_='fd8e9_1qWnZ')
# data = mid_content.find_all('a')
# print(data)