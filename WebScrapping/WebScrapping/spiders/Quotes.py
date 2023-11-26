import scrapy
from pathlib import Path

class QuotesSpider(scrapy.Spider):
    name = "Quotes"

    start_urls = []

    for i in range(1,11):
        urls = f"https://quotes.toscrape.com/page/{i}/"
        print(urls)
        start_urls.append(urls)
        
        
        
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
