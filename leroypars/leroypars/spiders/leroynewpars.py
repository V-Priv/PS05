import scrapy

class LeroynewparsSpider(scrapy.Spider):
    name = "leroynewpars"
    allowed_domains = ["lemanapro.ru"]
    start_urls = ["https://lemanapro.ru/catalogue/osveshchenie/"]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.5',  # Добавленный заголовок
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse, errback=self.error_handler)

    def parse(self, response):
        # Проверяем статус ответа
        status = response.status
        if status != 200:
            self.logger.error(f'Request failed with status code: {status}')

        # Проверяем наличие ошибок в ответе
        errors = response.css('.error-message').getall()
        if errors:
            self.logger.error(f'Errors found in response: {errors}')
        else:
            self.logger.info('No errors found in response')

    def error_handler(self, failure):
        if failure.check(scrapy.spidermiddlewares.httperror.HttpError):
            response = failure.value.response
            status = response.status
            self.logger.error(f'Request failed with status code: {status}')
        else:
            self.logger.error(f'Error occurred: {repr(failure)}')



