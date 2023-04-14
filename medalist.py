import scrapy


class MedalistSpider(scrapy.Spider):
    name = 'medalist'
    allowed_domains = ['wikipedia.org']
    start_urls = ['http://wikipedia.org/']

    def parse(self, response):
        pass
