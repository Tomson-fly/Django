import scrapy
import random
import requests
from ke.items import KeItem
from ke.settings import DEFAULT_REQUEST_HEADERS,IP_PROXY_LIST
from time import sleep


class KeSecSpider(scrapy.Spider):
    name = 'ke_sec'
    # allowed_domains = ['bj.zu.ke.com.cn']
    start_urls = [f'https://bj.ke.com/ershoufang/pg{i}' for i in range(1,101)]

    def start_requests(self):
        # response = requests.get('https://bj.fang.ke.com/')
        response = requests.get('https://bj.ke.com/')
        cookies = response.cookies

        self.cookie = requests.utils.dict_from_cookiejar(cookies)
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse,cookies=self.cookie)

    def parse(self, response):

        div = response.xpath("//div[@class='info clear']")
        all_msg = response.xpath("//div[@class='address']")
        for msg in all_msg:
            item = KeItem()
            # 位置（小区名）community = models.CharField(max_length=50)
            loc = msg.xpath("div[@class='flood']/div/a/text()").extract()[0]
            # 价格price = models.IntegerField()
            price = int(msg.xpath("div[@class='priceInfo']/div[@class='totalPrice']/span/text()").extract()[0].strip())

            info = msg.xpath("div[@class='houseInfo']/text()").extract()[-1]
            # built = info.split('建')[0].split('|')[-1].strip()
            # 建筑建成时间built
            area = info.split('平米')[0].split('|')
            # 户型type = models.CharField(max_length=10)
            type = area[-2].strip().split()[-1]
            # 面积area = models.FloatField()
            area = float(area[-1].strip())

            item['community'] = loc
            item['price'] = price
            item['type'] = type
            item['area'] = area
            # item['community'] = loc
            # item['metro'] = metro
            # item['heating'] = heating
            # item['decoration'] = decoration
            # item['showing'] = showing

            yield item
