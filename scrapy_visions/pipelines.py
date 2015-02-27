# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem

#remove duplicate products with the same id
class ScrapyVisionsPipeline(object):
    def __init__(self):
        self.ids_seen = set()
    def process_item(self, item, spider):
        if item['product_id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['product_id'])
            return item 
