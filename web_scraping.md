# Web Scraping Tools

## HTML extraction: BeautifulSoup
```
from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
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


