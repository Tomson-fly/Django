# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
from house.models import *
import scrapy


class KeItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # django_model = new
    # django_model = rent
    django_model = sec
