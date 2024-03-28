import scrapy
import requests
import random
from ke.items import KeItem
from ke.settings import DEFAULT_REQUEST_HEADERS,IP_PROXY_LIST
from time import sleep
class KeNewSpider(scrapy.Spider):
    name = 'ke_new'
    # allowed_domains = ['bj.zu.ke.com.cn']
    start_urls = [f'https://bj.fang.ke.com/loupan/pg{i}/' for i in range(1,26)]

    def start_requests(self):
        response = requests.get('https://bj.fang.ke.com/')
        cookies = response.cookies

        self.cookie = requests.utils.dict_from_cookiejar(cookies)
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse,cookies=self.cookie)

    def parse(self, response):
        sleep(0.5+random.random())
        '/html/body/div[6]/ul[2]/li[2]'
        all_msg = response.xpath("//div[@class='resblock-desc-wrapper']")
        for msg in all_msg:
            name = msg.xpath("div[@class='resblock-name']/a")
            href = 'https://bj.fang.ke.com' + name.attrib['href']
            name = name.attrib['title']
            # loc = msg.xpath("a[@class='resblock-location']").attrib['title']
            price = msg.xpath("div[@class='resblock-price']/div/span/text()").extract()[0]

            meta = {
                'name': name,
                # 'loc': loc,
                'price': price,
            }

            yield scrapy.Request(url=href, callback=self.parse_detail,
                                 headers=DEFAULT_REQUEST_HEADERS, cookies=self.cookie, meta=meta)

    def parse_detail(self, response):
        text = response.text

        all_msg = response.xpath("//div[@class='card-content']")
        if all_msg:
            for msg in all_msg:
                item = KeItem()
                price = int(msg.xpath("div[@class='content-price']/span/text()").extract()[0])
                type = msg.xpath("div[@class='content-title']/text()").extract()[0].strip()
                area = msg.xpath("div[@class='content-area']/text()").extract()[0]
                area = float(area.split("（")[0][2:-3])
                item['price'] = price
                item['area'] = area
                item['type'] = type
                yield item
        else:
            item = KeItem()
            item['community'] = response.meta['name']
            item['price'] = response.meta['price']
            item['area'] = 0
            item['type'] = 'unknown'
            return item