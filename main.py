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
    except Exception as e:
        return None
    return bs

site = getSite('http://pythonscraping.com/pages/warandpeace.html')
nameList = site.find_all('span', {'class': 'green'})
site.find_all()
print(nameList)
a = set()
for name in nameList:
    a.add(name.get_text())
print (a)