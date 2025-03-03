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

## Requests
``
import requests
``

## GET request
```
response = requests.get("[https://example.com](https://example.com)")
```

# Check status code
```
print(response.status_code)  # 200 for success
```

# Get response content
```
print(response.text)  # HTML content
print(response.content) # raw bytes
```

# Get headers
```
print(response.headers)
```

# Get specific header
```
print(response.headers['Content-Type'])
```

# Get JSON content
```
try:
    data = response.json()
    print(data)
except ValueError:
    print("Response is not JSON")
```

# POST request
```
data = {"key": "value"}
response = requests.post("[https://example.com/submit](https://www.google.com/search?q=https://example.com/submit)", data=data)
```

# POST request with JSON
```
import json

json_data = {"key": "value"}
response = requests.post("[https://example.com/submit](https://www.google.com/search?q=https://example.com/submit)", json=json_data)

# Custom headers
headers = {"User-Agent": "My Custom User Agent"}
response = requests.get("[https://example.com](https://example.com)", headers=headers)

# Handling cookies
cookies = {"session_id": "12345"}
response = requests.get("[https://example.com](https://example.com)", cookies=cookies)

# Timeouts
try:
    response = requests.get("[https://example.com](https://example.com)", timeout=5) # 5 second timeout
except requests.exceptions.Timeout:
    print("Request timed out")

# Handling exceptions
try:
    response = requests.get("[https://nonexistent.example.com](https://www.google.com/search?q=https://nonexistent.example.com)")
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Downloading files
response = requests.get("[https://example.com/image.jpg](https://www.google.com/search?q=https://example.com/image.jpg)")
if response.status_code == 200:
    with open("image.jpg", "wb") as f:
        f.write(response.content)

```

