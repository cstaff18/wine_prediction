import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')
}

name_dict = {}

for n in range(509):

    page = requests.get("https://www.wine-searcher.com/biz/producers/usa?s={0}".format((n * 25)+1),headers = HEADERS)

    soup = BeautifulSoup(page.content,'html.parser')

    names = soup.find_all('td', {'class': 'wlrwdt wlbdrl vtop'})
    addresses = soup.find_all('td', {'class': 'wlrwdt vtop'})

    for i , _ in enumerate(names):
        ind_name = names[i]
        a_name = ind_name.find('a')
        winery_name = a_name.get_text()
        winery_address = addresses[3*i+1].find('small').get_text().strip()

        name_dict[winery_name] = winery_address.replace(',', '')

with open('name_dict.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in name_dict.items()]
