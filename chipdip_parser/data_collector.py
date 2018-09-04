import requests
from bs4 import BeautifulSoup


def page_exist_check(soup):
    exist = soup.find('table', {'class': 'filter-and-products'})
    return exist


def collect_items_data(soup):
    item_data = {}
    data_table = soup.find_all('tr', {'class': 'with-hover'})
    for item_data in data_table:
        try:
            name = item_data.find('a', {'class': 'link'}).text.strip()
        except:
            name = ''
        try:
            pps = soup.find('div', {'class': 'pps'}).strip()
        except:
            pps = ''
        item_data[name] = {'property': pps}
    return item_data


def collect_data(link, header):
    data = None
    for page_num in range(1, 100):
        url = link + '?locid=minsk-dimitrova-5&page=' + str(page_num)
        page = requests.get(url, headers=header)
        soup = BeautifulSoup(page.text, 'html.parser')
        exist = None
        exist = page_exist_check(soup)
        if exist is not None:
            data = collect_items_data(soup)
    return data
