import scrapy


class AranhaSpider(scrapy.Spider):
    name = "aranha"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["http://es.wikipedia.org/"]
#https://en.wikipedia.org/wiki/1992_World_Junior_Championships_in_Athletics_%E2%80%93_Men%27s_high_jump
    def parse(self, response):
        pass
