# coding:utf-8
from django.db import models
from django.contrib.auth.models import User


#  定义模块
class Benjamin(models.Model):
    name = models.CharField(u"板块名称", max_length=50)  # 获取板块名称，CharField获取的是字符串
    #  user_num = models.IntegerField(u"用戶代碼")
    desc = models.CharField(u"描述", max_length=300)  # 描述板块信息
    #  sex = models.IntegerField(u"性別", choices=((1, u"男"), (2, u"女")))  # 描述性别
    manager = models.ForeignKey(User, verbose_name="作者")  # 设置管理员

    creat_timestamp = models.DateTimeField(u"创建时间", auto_now_add=True)  # 以下两句为创建时间戳
    last_update_timestamp = models.DateTimeField(u"更新时间", auto_now=True)

#  定义首列
    def __unicode__(self):
        return self.name + "12345"


#  定义Mata类，为Benjamin模块定义名称
    class Meta:
        verbose_name = u"板块"
        verbose_name_plural = u"板块"
