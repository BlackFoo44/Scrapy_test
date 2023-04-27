import scrapy
import openpyxl

from .params_for_spider import start_url, url_for_next_page

class EnamelSpider(scrapy.Spider):
    name = "all_items"
    start_urls = [start_url]

    def parse(self, response, **kwargs):
        for link in response.css('div.name a::attr(href)'):
            yield response.follow(link, callback=self.parse_item)

        for i in range(2, 3):
            next_page = url_for_next_page+{i}
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response):
        yield {
            "name": response.css('h1::text').get(),
            "price": response.css('div.price_new span::text').get()
        }