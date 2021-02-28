from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup as bs4


def getSite(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None

    try:
        bs = bs4(html, 'html.parser')
    except AttributeError as e:
        return None

    return bs

site = getSite('https://www.moex.com/')
print(site.find_all('div')[4].find_all('img'))