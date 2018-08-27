import requests
from bs4 import BeautifulSoup
import time




url = 'https://www.ru-chipdip.by/catalog'
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.44'}
page = requests.get(url, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')
main_content = soup.find_all('div', {'class': 'catalog_g0 clear'})
soup_without_scratch = BeautifulSoup(str(main_content), features="html.parser")
departments = soup_without_scratch.find_all('a', {'class': 'link'})
departments_urls = []
subdeps_urls = {}

for department in departments:
    print(department)
    url = 'https://www.ru-chipdip.by' + department['href']
    departments_urls.append(url)
    x = department.split('">')
    x = x[1].split("</a>")
    print(x[0])
    subdeps_urls[department].append(url)
    department.find('p')
i = 0
for dep in departments_urls:
    if i == 5:
        break
    i += 1
    url = requests.get(dep, headers=header)
    soup = BeautifulSoup(url.content, 'html.parser')
    secondary_content = soup.find_all('div', {'class': 'catalog__g2'})
    soup_without_scratch = BeautifulSoup(str(secondary_content), features="html.parser")
    subdeps = soup_without_scratch.find_all('a', {'class': 'link'})
    for subdep in subdeps:
        subdeps_urls[dep].append('https://www.ru-chipdip.by' + subdep['href'])
        time.sleep(2)
print(subdeps_urls)

def page_exist_check(number, url):
    page = BeautifulSoup(url)
    if soup.find('div', {'class': 'profileFilmsList'}):
        return 'exist'

for dep in departments_urls:
    for subdep in subdeps:
        if page_exist_check(num, url)== 'exist':
            pass
