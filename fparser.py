import feedparser
d = feedparser.parse("http://www.aif.ru/rss/all.php")
e = d['items'][0]
a = d['channel']['title']
b = e['title']
c = e['description']
str = a + "\n"
str1 = b + "\n"
str2 = c + "\n"
str3 =
q = open('/home/dimka/Desktop/feedparse/feedparse3.txt', 'w')
q.write(str.encode("utf-8"))
q.write(str1.encode("utf-8"))
q.write(str2.encode("utf-8"))
q.close()