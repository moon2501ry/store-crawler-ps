from psstorecrawler import WebCrawler
import pyautogui as pg

num_input = input("NPage> ");
num_list = list(range(1, int(num_input)+1));

for nm in num_list:
    client = WebCrawler('https://store.playstation.com/pt-br/category/d0446d4b-dc9a-4f1e-86ec-651f099c9b29/'+str(nm));
    client.get_soup();
    games = client.crawler();