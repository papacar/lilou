# lilou

简洁的采集工具

## 依赖项目

- Beautifulsoup
- pandas
- numpy
- scrapy:
  - [文档资料](https://scrapy-chs.readthedocs.io/)

如果 Python 是通过 Anaconda 安装的，那么只需要再附加安装 scrapy

```bash
conda install scrapy
```

## NCBI 数据采集

```bash
cd ncbi
scrapy crawl ncbi_gene
```

### todo

- [ ] 解决内嵌表格异步加载问题
