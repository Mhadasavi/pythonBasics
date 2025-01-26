import urllib.request
from pprint import pprint

from html_table_parser import HTMLTableParser


def url_get_contents(url):
    # Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    req = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    f = urllib.request.urlopen(req)

    return f.read()


xhtml = url_get_contents('https://crypto.com/price').decode('utf-8')

p = HTMLTableParser()

p.feed(xhtml)
# print(len(p.tables))
pprint(p.tables[0])