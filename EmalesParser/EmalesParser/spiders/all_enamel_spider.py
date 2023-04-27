import scrapy
import openpyxl
from .params_for_spider import start_url, url_for_next_page, scrapy_item, pars_parametr, pars_parametr1


class EnamelSpider(scrapy.Spider):
    name = "all_enamel"
    start_urls = [start_url]

    def parse(self, response, **kwargs):
            for link in response.css(scrapy_item):
                    yield response.follow(link, callback=self.parse_item)

            while True:
                i = 1
                if response.css('a.modern-page-next ::attr(href)').get():
                    next_page = url_for_next_page+str(i)
                    yield response.follow(next_page, callback=self.parse)
                i += 1


    def parse_item(self, response):
        yield {
            "name": response.css(pars_parametr).get(),
            "price": response.css(pars_parametr1).get()
        }