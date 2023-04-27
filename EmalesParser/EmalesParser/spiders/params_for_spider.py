start_url = "https://krasn.russcvet.ru/catalog/enamels/"
url_for_next_page = "https://krasn.russcvet.ru/catalog/enamels/?PAGEN_1="



scrapy_item = 'div.name a::attr(href)'
"""
Необходимо указать 'tag.class tag::attr(атрибут в котором лежит ссылка на объект)'
"""

"""
Необходимо указать 'tag.class tag::text'
"""
pars_parametr = 'h1::text'
pars_parametr1 = 'div.price_new span::text'
