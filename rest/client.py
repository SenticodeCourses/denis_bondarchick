import requests
import flask_routes
from bs4 import BeautifulSoup
from threading import Thread


class Input(Thread):
    def __init__(self, domain):
        Thread.__init__(self)
        self.domain = domain
        self.header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) OPR/55.0.2994.44'}

    def run(self):
        # self.daemon = True
        while True:
            flask_routes.start()

    def get(self, url):
        page = requests.get(url, headers=self.header)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup)
