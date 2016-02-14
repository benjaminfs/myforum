# coding:utf-8
from django.db import models
from django.contrib.auth.models import User


class benjamin(models.Model):
    user_name = models.CharField(u"用戶名", max_length=50)
    user_num = models.IntegerField(u"用戶代碼")
    sex = models.IntegerField(u"性別", choices=((1, u"男"), (2, u"女")))
    owner = models.ForeignKey(User, verbose_name="作者")

    creat_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user_name
