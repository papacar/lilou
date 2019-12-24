import re
import requests
from bs4 import BeautifulSoup


base_urls = ['https://www.ncbi.nlm.nih.gov/gene/?term=']


def touch_page(url):
    sub_urls = []
    home_page_html = requests.get(url)
    home_page_html.encoding = 'utf-8'
    soup = BeautifulSoup(home_page_html.text, 'lxml')
    table_text = soup.select('.ui-ncbigrid-inner-div')
    for table_context in table_text:
        parse_table(table_context)


def parse_table(table_context):
    soup = table_context
    item_header = soup.find_all('thead')
    table_body = soup.find('tbody')
    item_list = soup.find_all('tr', attrs={'class': 'rprt'})
    for item in item_list:
        for td in item.find_all('td'):
            print(td, end='\t|\t')
        print('\n', '-'*30)


if __name__ == "__main__":
    touch_page('https://www.ncbi.nlm.nih.gov/gene/?term=s30')
