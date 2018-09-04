from link_collector import collect_links
from data_collector import collect_data
from save_file import save


url = 'https://www.ru-chipdip.by/catalog'
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) OPR/55.0.2994.44'}
links = collect_links(url, header)
for key in links.keys():
    for dept in links[key]:
        item_data = collect_data(dept, header)
        data_dict = {key: { dept: { item_data }        }        }
        save(data_dict)
