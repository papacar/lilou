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
    print('| Gene Name | ID | Gene Url |\n|:---:|:---:|:---:|')
    for item in item_list:
        div_gene_id(item.find_all('td')[0])
        # for td in item.find_all('td'):
        # print('-'*30)


def parse_item(item):
    id_gene = item[0]
    div_gene_id(id_gene)
    descrip = item[1]
    localtion = item[2]
    aliases = item[3]
    mim = item[4]


def div_gene_id(gene_item):
    item_strings = [t for t in gene_item.strings]
    gene_name = item_strings[1]
    gene_id = re.findall(r'ID: (\d+)', item_strings[2])[0]
    gene_url = gene_item.find_all('a')[0].get('href')
    print('| ', gene_name, ' | ', gene_id, ' |', gene_url, ' |')


if __name__ == "__main__":
    touch_page('https://www.ncbi.nlm.nih.gov/gene/?term=s30')
    # test_str = """<td class="gene-name-id"><div class="rprtnumcol"><div class="rprtnum nohighlight"><label class="ui-helper-hidden-accessible" for="UidCheckBox100410858">Select item 100410858</label><input id="UidCheckBox100410858" name="EntrezSystem2.PEntrez.Gene.Gene_ResultsPanel.Gene_TabularDocsum.uid" sid="16" type="checkbox" value="100410858"/></div></div><div><a href="/gene/100410858" ref="ordinalpos=16&amp;ncbi_uid=100410858&amp;link_uid=100410858">FAU</a></div><span class="gene-id">ID: 100410858</span></td>"""
    # soup = BeautifulSoup(test_str, 'lxml')
    # for t_str in soup.strings:
    #     print(t_str)
