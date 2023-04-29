import scrapy

from .parametrs_for_parses import ParamsForParser

params = ParamsForParser(
    name="first_16_enamels",
    url="https://krasn.russcvet.ru/catalog/enamels/",
    allowed_domains="",
    item_link="div.name a::attr(href)",
    pagen="",
    item_header={"item_name": "h1::text", "item_price": "div.price_new span::text"})

class EnamelSpider(scrapy.Spider):
    name = params.name
    start_urls = [params.url]

    def parse(self, response, **kwargs):
        for link in response.css(params.item_link):
            yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response):
        yield {
            "name": response.css(params.item_header["item_name"]).get(),
            "price": response.css(params.item_header["item_price"]).get(),
        }
