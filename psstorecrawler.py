import requests as re
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self,url):
        self.url = re.get(url).content;

    def get_soup(self):
        self.soup = BeautifulSoup(self.url, 'html.parser');

    def crawler(self):
        self.game_name = self.soup.select('span.psw-t-body.psw-c-t-1.psw-t-truncate-2.psw-m-b-2')
        with open('game.txt', 'a') as txt:
            for name in self.game_name:
                print(name.text);
                txt.write(name.text+'\n');
        return self.game_name;