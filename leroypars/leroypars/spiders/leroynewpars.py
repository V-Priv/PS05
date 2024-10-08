import scrapy


class LeroynewparsSpider(scrapy.Spider):
    name = "leroynewpars"
    allowed_domains = ["https://lemanapro.ru"]
    start_urls = ["https://lemanapro.ru/catalogue/osveshchenie/"]

    def parse(self, response):
        pass
