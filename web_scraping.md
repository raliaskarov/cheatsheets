# Web Scraping Tools

## HTML extraction option 1: BeautifulSoup
```
from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
```

## HTMP extraction option 2: Pandas
```
import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(URL)
df = tables[0]
print(df)
```

## Web Crawling: Scrapy
```
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}
```

## Web Browsers Control: Selenium
```
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.example.com")
```


