from django.db import models

# Create your models here.


# 轮播图
class Wheel(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=30)


# 导航
class Nav(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=30)


# 每日必抢
class Mustbuy(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=30)


# 便利店
class Shop(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=30)


# 分类模型
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=200)
    typename = models.CharField(max_length=200)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()


# 商品模型类
class Goods(models.Model):
    productid = models.CharField(max_length=200)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    productlongname = models.CharField(max_length=200)
    # 是否精选
    isxf = models.NullBooleanField(default=False)
    # 是否买一赠一
    pmdesc = models.CharField(max_length=200)
    # 规格
    specifics = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    marketprice = models.CharField(max_length=200)
    # 组ID
    categoryid = models.CharField(max_length=200)
    # 子类组ID
    childcid = models.CharField(max_length=200)
    childcidname = models.CharField(max_length=200)
    # 详情页ID
    dealerid = models.CharField(max_length=200)
    # 库存
    storenums = models.IntegerField()
    # 销量
    productnum = models.IntegerField()


class User(models.Model):
    useraccount = models.CharField(max_length=200, unique=True)
    userpasswd = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    userphone = models.CharField(max_length=200)
    useradderss = models.CharField(max_length=200)
    userimg = models.CharField(max_length=200)
    userrank = models.IntegerField()
    usertoken = models.CharField(max_length=200)

    @classmethod
    def createuser(cls, account, passwd, name, phone, address, img, rank, token):
        u = cls(useraccount=account, userpasswd=passwd, username=name, userphone=phone,
                useradderss=address, userimg=img, userrank=rank, usertoken=token)
        return u


class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isdelete=False)


class Cart(models.Model):
    useraccount = models.CharField(max_length=200)
    productid = models.CharField(max_length=200)
    productnum = models.IntegerField()
    productprice = models.CharField(max_length=200)
    ischose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    orderid = models.CharField(max_length=200, default='0')
    isdelete = models.BooleanField(default=False)

    objects = CartManager1()
    # object2 = CartManager2
    @classmethod
    def createcart(cls, useraccount, productid, productnum, productprice, ischose,
                   productimg, productname, isdelete):
        c = cls(useraccount=useraccount, productid=productid, productnum=productnum,
                productprice=productprice, ischose=ischose, productimg=productimg,
                productname=productname, isdelete=isdelete)
        return c


class Order(models.Model):
    orderid = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    progress = models.IntegerField()

    @classmethod
    def createorder(cls, orderid, userid, progress):
        o = cls(orderid=orderid, userid=userid, progress=progress)
        return o
