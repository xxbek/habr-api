import re
import requests
from bs4 import BeautifulSoup

# url = 'http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
#            }
# req = requests.get(url, headers=headers)
# src = req.text

with open('index.html', 'r') as file:
    src = file.read()

soup = BeautifulSoup












# with open('blank/index.html', 'r') as f:
#     src = f.read()
#
# soup = BeautifulSoup(src, 'lxml')
#
# title = soup.title
# page_h1 = soup.find_all('h1')
#
# user_name = soup.find('div', class_='user__name')
#
# user_name = soup.find('div', {'class': 'user__name'}).find('span').text
#
# find_all_span_inUser_info = soup.find(class_='user__info').find_all('span')
#
# # find_parent, find_parents
#
# # next_element - find_next, previous_element
#
# # find_next_sibling(), find_previous_sibling - братья и сестры
#
# find_a_by_text = soup.find('a', text=re.compile('Одежда'))
#
#
# find_all_clothes = soup.find_all(text=re.compile('[Оо]дежда'))
# print(find_all_clothes)
