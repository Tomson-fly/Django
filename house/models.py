from django.db import models

# Create your models here.
# 用户类
class user(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class rent(models.Model):
    # 整/合
    joint = models.BinaryField()
    # 租金
    price = models.IntegerField()
    # 户型
    type = models.CharField(max_length=10)
    # 面积
    area = models.FloatField()
    # 朝向
    orientation = models.CharField(max_length=10)
    # 位置（小区名）
    community = models.CharField(max_length=50)
    # 近地铁
    metro = models.BinaryField()
    # 集中供暖
    heating = models.BinaryField()
    # 精装修
    decoration = models.BinaryField()
    # 随时看房
    showing = models.BinaryField()

    location = models.CharField(max_length=10, null=True)

class new(models.Model):
    # 参考价格
    price = models.IntegerField()
    # 户型
    type = models.CharField(max_length=10)
    # 面积
    area = models.FloatField()
    # 位置（小区名）
    community = models.CharField(max_length=50)

    location = models.CharField(max_length=10, null=True)

class sec(models.Model):
    # 价格
    price = models.IntegerField()
    # 户型
    type = models.CharField(max_length=10)
    # 面积
    area = models.FloatField()
    # 位置（小区名）
    community = models.CharField(max_length=50)

    location = models.CharField(max_length=10, null=True)
    # # 建筑建成时间
    # built = models.DateField()

class buyinfo(models.Model):
    name = models.CharField(max_length=30)

    idcard = models.CharField(max_length=18)
    phone = models.CharField(max_length=11)
    money = models.IntegerField()
    renttime = models.CharField(max_length=5)
