# -*- coding: utf-8 -*-
import scrapy

#holds product information from visions.ca
class ScrapyVisionsItem(scrapy.Item):
    product_id = scrapy.Field()
    category = scrapy.Field()    
    product_code = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    
 