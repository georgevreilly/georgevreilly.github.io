#!/usr/bin/env python

import codecs
import pprint
import os
import requests
import bs4
import urlparse

BASE_URL = "http://localhost:8080/"


def parse_dasblog_permalinks(html):
    link_prefix = urlparse.urljoin(BASE_URL, "/20")
    laquo, raquo = unichr(171), unichr(187)
    soup = bs4.BeautifulSoup(html)
#   items = soup.select('div.items a.href^="http://localhost:8080/"')
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            href = link['href']
            if href.startswith(link_prefix):
                text = link.get_text()
                if text.startswith(laquo):
                    yield (href, text[2:])
                elif text.endswith(raquo):
                    yield (href, text[:-2])


def scrape_dasblog_permalinks(url):
    response = requests.get(url)
    return parse_dasblog_permalinks(response.text)


if __name__ == '__main__':
    start_url = urlparse.urljoin(BASE_URL, "/2013/12/17/JoiningCookBrite.aspx")
    permalinks = {}
    limit = 15000
    count = 0
    queue = [start_url]
    while queue:
        url = queue.pop(0)
        print url
        for link, title in scrape_dasblog_permalinks(url):
            if not link in permalinks and count < limit:
                permalinks[link] = title
                queue.append(link)
                count += 1

    with codecs.open(os.path.join(os.path.dirname(__file__), "permalinks.json"),
            "w", encoding="utf8") as fp:
        fp.write(u"{\n")
        for link in sorted(permalinks.keys()):
            fp.write(u'    "{0}": "{1}",\n'.format(link[len(BASE_URL)-1:], permalinks[link]))
        fp.write(u"}\n")
