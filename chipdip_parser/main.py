from link_collector import collect_links
from data_collector import collect_data


url = 'https://www.ru-chipdip.by/catalog'
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.44'}
links = collect_links(url, header)
for key in links.keys():
    for link in links[key]:
        print(link)
        collect_data(link, header)
        break
    break