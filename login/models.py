from django.db import models


# Create your models here.

class ProductInfo(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    ps = models.CharField(max_length=256, blank=True, null=True, default='暂无备注！')

# 创建表时，相当于 create table login_ProductInfo(id bigint auto_increment primary key,name varchar(32),price int)
# 数据默认为空，且必须填写
# (null=True,blank=True)

# 1.新建数据 insert into login_productinfo(name,price) values("香蕉", 31)
# ProductInfo.objects.create(name="香蕉", price=31)

# 2。删除数据
# ProductInfo.objects.filter(id=3).delete()
# filter是筛选条件用
# ProductInfo.objects.all().delete() 是全删

# 3.获取数据
# (QuerySet型，对象集型)data_list = [对象(封装了一行数据)，对象，对象]
# data_list = ProductInfo.objects.all() 获取全部数据<=> select * from
# 也能筛选 data_list = ProductInfo.objects.filter(id=1) 获取id=1的数据，依然是QuerySet型，是对象集
# data_list = ProductInfo.objects.filter(id=1).first() #第一条数据，不是QuerySet型，是一个对象

# 4.更新数据
# ProductInfo.object.all().update(price=3) 全部更新
# ProductInfo.object.filter(id=1).update(price=3) 更新id=1


class UserInfo(models.Model):
    usr = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
