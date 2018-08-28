import requests
from bs4 import BeautifulSoup
import time

def page_exist_check(soup):
    exist = soup.find('table', {'class': 'filter-and-products'})
    return exist

def collect_items_data(soup):
    data_table = soup.find_all('tr', {'class': 'with-hover'})
    for item_data in data_table:
        try:
            name = item_data.find('a', {'class': 'link'}).text  #strip?
        except:
            name = ''
        try:
            pps = soup.find('div', {'class': 'pps'})
        except:
            pps = ''
        page_data = {'name': name, 'property': pps}
        break
    return page_data

# def collect_items(soup):
#     data_table = soup.find_all('tr', {'class': 'with-hover'})
#     return data_table

def collect_data(link, header):
    for page_num in range(1, 2):
        url = link + '?page=' + str(page_num)
        page = requests.get(url, headers=header)
        soup = BeautifulSoup(page.text, 'html.parser')
        if page_exist_check(soup):
            collect_items_data(soup)
        break
    # return page_data

