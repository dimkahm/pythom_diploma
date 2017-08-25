import re
import feedparser

def entrylog(entry):
    "publication-time&date:author:link"
    msg = 'title: ' + entry.title + ' - link: ' + entry.link + ' - author: ' + entry.author # + '\ncontent:\n' + entry.summary
    print msg

regex_key = re.compile('entrainment|music* performance|interpersonal|multimodal*|expressive*|coordination')
rssfeed = ['http://mp.ucpress.edu/rss/recent.xml','http://pom.sagepub.com/rss/recent.xml','http://www.cell.com/trends/cognitive-sciences/inpress.rss','http://www.cell.com/trends/cognitive-sciences/current.rss','http://journal.frontiersin.org/journal/psychology/rss']

total = 0

for i in rssfeed:
    d = feedparser.parse(i) # read link at a time
    for post in d.entries:  # read one RSS entry at a time
        try: # some feeds may not have summary
            m = re.search(regex_key, post.title)  # match regex in title
            n = re.search(regex_key, post.summary)  # match regex in summary
        except:
            print 'WARNING: The entry ' + post.title + ' at: ' + post.id + ' has no summary'

        if ((m != None)|(n != None)):
            entrylog(post)

    print str(len(d['entries'])) + " entries scanned from: " + d['feed']['title']
    total = len(d['entries']) + total
print "Total entries = ", total