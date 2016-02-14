# coding:utf-8
from django.contrib.auth.models import User
from django.db import models


class Demo(models.Model):
    example4char = models.CharField(u"字符範例", max_length=30)
    example4int = models.IntegerField(u"數字範例")
    sex = models.IntegerField(u"性別", choices=((1, u"男"), (2, u" 女")))
    owner = models.ForeignKey(User, verbose_name="作者")

    create_timestamp = models.DateField(auto_now_add=True)
    last_update_timestamp = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.example4char
