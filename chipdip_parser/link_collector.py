import requests
from bs4 import BeautifulSoup
import time
import random
links = {}


def collect_dept_link(url, header):
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    departments = soup.find_all('div', {'class': 'catalog__g2'})
    for department in departments:
        dept_link = 'https://www.ru-chipdip.by' + department.find('a', {'class': 'link'}).get('href')
        # dept_name = department.find('a', {'class': 'link'}).text
        links[dept_link] = []
    print('Колькасць атрыманых раздзелаў:', len(links))
    return links


def collect_subdept_links(url, header):
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    subdepts = soup.find_all('div', {'class': 'catalog__g2'})
    for subdept in subdepts:
        subdept_link = 'https://www.ru-chipdip.by' + subdept.find('a', {'class': 'link'}).get('href')
        links[url].append(subdept_link)
    print('Колькасць атрыманых падраздзелаў у раздзелe', url, len(subdepts))
    return links


def collect_links(url, header):
    dept_links = collect_dept_link(url, header)
    links_with_subdepts = {}
    i = 0
    for dept in dept_links.keys():
        if i < 2:
            links_with_subdepts = collect_subdept_links(dept, header)
            time.sleep(random.randint(1, 3))
            i += 1
    return links_with_subdepts
