
x = xmlParser(source_path='http://news.yandex.ru/world.rss', source_type='xml')
for i in x.getData(['.*/a'], get_attrib=True):
    if i[1] and 'href' in i[1]:
        print i[1] ['href']