# coding: utf-8
from lxml.html import parse
page = parse('http://habrahabr.ru/').getroot()
hrefs = page.cssselect("a.topic")
for row in hrefs:
    print row.get("href")