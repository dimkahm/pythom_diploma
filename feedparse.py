# coding: utf-8
import re
import urllib
from psycopg2 import connect

regexp = r"<item>.+</link>\s+<title>([А-Яа-я0-9]\s*#\d*)</title>.+</pubDate>\s+<description><!\[CDATA\[(.,+:;)\]\]>\s*</description>\s+</item>"
f = open('/home/dimka/Desktop/feedparse/feedparse.csv','w')
def take_rss(a):
	rss_text = urllib.urlopen(a).read()
	f.write(rss_text)
	f.close()
	f1 = open('/home/dimka/Desktop/feedparse/feedparse.csv','r')
	rss_text = f1.read()
	rss = re.findall(regexp,rss_text)
	print rss

feed = "http://news.yandex.ru/index.rss"#raw_input("Введите ссылку на фид.\n")#http://bash.org.ru/rss/

take_rss(feed)
#f2  = open('/home/dimka/Desktop/feedparse/feedparse.csv','r')
