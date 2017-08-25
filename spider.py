import lxml
import re
import bs4
from news.items import NewsItem
from scrapy.item import Item, field
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Compose
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.selector import HtmlXPathSelector
class NewsLoader (XPathItemLoader):
    default_input_processor = MapCompose(lambda s: re.sub('\s+', ' ', s.strip()))
    default_output_processor = TakeFirst()

class NewsSpider(CrawlSpider) :
    name = "news"
    allowed_domains = ["news.yandex.ru"]
    start_urls = ["http://news.yandex.ru/index.rss"]

rules = (
    Rule(SgmlLinkExtractor(allow=()), follow=True)
    Rule(SgmlLinkExtractor(allow=()), callback='parse_item'),


)
class NewsItem(Item):
    id = Field()
    title = Field()
    link = Field()
    category = Field()
    guid = Field()
    category_id = Field()
    pubDate = Field()
    description = Field()