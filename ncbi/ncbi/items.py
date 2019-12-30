# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NcbiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gene_name = scrapy.Field()
    gene_link = scrapy.Field()
    gene_id = scrapy.Field()
    desc = scrapy.Field()
