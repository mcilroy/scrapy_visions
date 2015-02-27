import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy_visions.items import ScrapyVisionsItem
import time
from bs4 import BeautifulSoup
import re
#spider built to crawl visions.ca
class VisionsSpider(CrawlSpider):
    name = "visions"
    allowed_domains = ["visions.ca"]
    start_urls = [
        "http://www.visions.ca"
    ]
    rules = [
        Rule(LinkExtractor(allow=['/Catalogue/Category/Default.aspx\.*']), 'parse_category'),
        ]
    #parse files, ignore the files from the main category pages, they'll fail on the category
    def parse_category(self, response):
        soup = BeautifulSoup(response.body)
        try:
            category = soup.find(id='ctl00_pnlBreadCrumbs').find('span').string
            for box in soup.find(id='ctl00_tdMainPanel').find_all("div", class_="productresult-itembox"):
                content_right = box.find_all("div", class_="contentright")[0]
                a = content_right.find("h2").find("a")
                href = a.get("href")
                item = ScrapyVisionsItem()
                item['product_id'] = re.compile(".*productId=(\d+).*").findall(href)[0]
                item['category'] = category
                item['product_code'] = a.find("span").find("span").string
                item['product_name'] = a.find("font").contents[0]
                item['product_price'] = content_right.find("span", class_="price").string
                yield item
        except AttributeError:
            print("attribute error")


