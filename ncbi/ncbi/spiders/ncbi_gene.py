# -*- coding: utf-8 -*-
import scrapy

from ncbi.items import NcbiItem
import re
import requests
from bs4 import BeautifulSoup
import logging


logger = logging.getLogger(__file__)

class NcbiGeneSpider(scrapy.Spider):
    name = 'ncbi_gene'
    allowed_domains = ['www.ncbi.nlm.nih.gov']
    start_urls = ['https://www.ncbi.nlm.nih.gov/gene/?term=s30']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True)

    def parse(self, response):
        logger.info("Request Headers is: {}".format(response.request.headers))
        soup = BeautifulSoup(response.text, 'lxml')
        table_text = soup.select('.ui-ncbigrid-inner-div')

        for table_context in table_text:
            self.parse_table(table_context)

        next_page = response.css('div.pagination a::attr(href)').get()
        logger.info("Get next_page is {}".format(next_page))
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_table(self, table_context):
        soup = table_context
        item_header = soup.find_all('thead')
        table_body = soup.find('tbody')
        item_list = soup.find_all('tr', attrs={'class': 'rprt'})
        print('| Gene Name | ID | Gene Url |\n|:---:|:---:|:---:|')
        for item in item_list:
            self.div_gene_id(item.find_all('td')[0])

    def div_gene_id(self, gene_item):
        item_strings = [t for t in gene_item.strings]
        gene_name = item_strings[1]
        gene_id = re.findall(r'ID: (\d+)', item_strings[2])[0]
        gene_url = gene_item.find_all('a')[0].get('href')
        print('| ', gene_name, ' | ', gene_id, ' |', gene_url, ' |')
