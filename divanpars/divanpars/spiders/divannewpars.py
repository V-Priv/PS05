import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Обходим каждый элемент освещения на странице
        for lamp in response.css('div.WdR1o'):
            # Извлекаем название
            name = lamp.css('div.lsooF span::text').get()

            # Извлекаем цену
            price = lamp.css('div.pY3d2 span::text').get()

            # Извлекаем ссылку
            link = lamp.css('a::attr(href)').get()
            if link:
                link = response.urljoin(link)  # Приводим относительную ссылку к абсолютной

            # Формируем словарь с данными
            yield {
                'name': name,
                'price': price,
                'link': link
            }

        # Пагинация: если есть следующая страница, следуем по ссылке
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
