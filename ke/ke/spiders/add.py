import scrapy


class AddSpider(scrapy.Spider):
    name = 'add'
    # allowed_domains = [''ke.com'']
    start_urls = ['https://ajax.api.ke.com/sug/headerSearch?channel=xiaoqu&cityId=110000&query=']

    def parse(self, response):
        pass
