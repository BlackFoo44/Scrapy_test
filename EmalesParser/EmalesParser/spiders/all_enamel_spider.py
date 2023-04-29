import scrapy
from .parametrs_for_parses import ParamsForParser

params = ParamsForParser(
    name="all_enamels",
    url="https://krasn.russcvet.ru/catalog/enamels/",
    allowed_domains="krasn.russcvet.ru",
    item_link="div.name a::attr(href)",
    pagen="https://krasn.russcvet.ru/catalog/enamels/?PAGEN_1=",
    item_header={"item_name": "h1::text", "item_price": "div.price_new span::text"})

class EnamelSpider(scrapy.Spider):
    name = params.name
    start_urls = [params.url]
    allowed_domains = [params.allowed_domains]
    def parse(self, response, **kwargs):
        for link in response.css(params.item_link):
            yield response.follow(link, callback=self.parse_item)

        for i in range(1, 56): #Необходимо указать колличество страниц для парсинга
            next_page = params.pagen + str(i)
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response):
        yield {
            "name": response.css(params.item_header["item_name"]).get(),
            "price": response.css(params.item_header["item_price"]).get(),
        }
