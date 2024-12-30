from psstorecrawler import WebCrawler
import pyautogui as pg

def msg(msgs):
    pg.moveTo(700,700);
    pg.leftClick();
    for m in msgs:
        pg.write(m.text);

num_input = input("NPage> ");
num_list = list(range(1, int(num_input)+1));

for nm in num_list:
    client = WebCrawler('https://store.playstation.com/pt-br/category/d0446d4b-dc9a-4f1e-86ec-651f099c9b29/'+str(nm));
    client.get_soup();
    games = client.crawler();

if input("SendMsgs(y or n)> ") == 'y':
    print('Sending Mensages...');
    input("Are you confirm?> ");
    msg(games);