import scrapy
import random
import requests
from ke.items import KeItem
from ke.settings import DEFAULT_REQUEST_HEADERS,IP_PROXY_LIST
from time import sleep

class KeRentSpider(scrapy.Spider):
    name = 'ke_rent'
    # allowed_domains = ['bj.zu.ke.com.cn']
    start_urls = [f'https://bj.zu.ke.com/zufang/pg{i}/#contentList/' for i in range(1,101)]

    def start_requests(self):
        # response = requests.get('https://bj.fang.ke.com/')
        response = requests.get('https://bj.zu.ke.com/')
        cookies = response.cookies

        self.cookie = requests.utils.dict_from_cookiejar(cookies)
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse,cookies=self.cookie)

    def parse(self, response):

        div = response.xpath("//div")
        all_msg = response.xpath("//div[@class='content__list--item--main']")
        for msg in all_msg:
            item = KeItem()
            title = msg.xpath("p[@class='content__list--item--title']/a/text()").extract()[0].strip().split(' ')
            joint = title[0].split('·')
            loc = joint[1]
            joint = joint[0]
            type = title[1]
            orien = title[2]
            if joint=='整租':
                joint = False
            else:
                joint = True
            des = msg.xpath("p[@class='content__list--item--des']/text()").extract()
            des = ''.join(des)
            area = float(des.split('㎡')[0].split(' ')[-1].strip())
            tag = msg.xpath("p[@class='content__list--item--bottom oneline']")
            # metro
            metro = bool(tag.xpath("i[@class='content__item__tag--is_subway_house']"))
            # 集中供暖-heating
            heating = bool(tag.xpath("i[@class='content__item__tag--central_heating']"))
            # 精装修-decoration
            decoration = bool(tag.xpath("i[@class='content__item__tag--decoration']"))
            # 随时看房-showing
            showing = bool(tag.xpath("i[@class='content__item__tag--is_key']"))

            # brand = msg.xpath("p[@class='content__list--item--brand oneline']/span/text()").extract()[0].strip()
            price = int(msg.xpath("span/em/text()").extract()[0])
            item['joint'] = joint
            item['price'] = price
            item['type'] = type
            item['area'] = area
            item['orientation'] = orien
            item['community'] = loc
            item['metro'] = metro
            item['heating'] = heating
            item['decoration'] = decoration
            item['showing'] = showing

            yield item

# # 整/合
#     joint = models.BinaryField()
#     # 租金
#     price = models.IntegerField()
#     # 户型
#     type = models.CharField(max_length=10)
#     # 面积
#     area = models.FloatField()
#     # 朝向
#     orientation = models.CharField(max_length=10)
#     # 位置（小区名）
#     community = models.CharField(max_length=50)
#     # 近地铁
#     metro = models.BinaryField()
#     # 集中供暖
#     heating = models.BinaryField()
#     # 精装修
#     decoration = models.BinaryField()
#     # 随时看房
#     showing = models.BinaryField()
