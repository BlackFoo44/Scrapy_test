import scrapy
import openpyxl

from .params_for_spider import start_url, scrapy_item, pars_parametr, pars_parametr1


class EnamelSpider(scrapy.Spider):
    name = "16_enamels"
    start_urls = [start_url]

    def parse(self, response, **kwargs):
        for link in response.css(scrapy_item):
            yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response):
        yield {
            "name": response.css(pars_parametr).get(),
            "price": response.css(pars_parametr1).get()
        }
