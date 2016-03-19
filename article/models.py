#  coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from buluojianshe.models import Benjamin


class Article(models.Model):
    block = models.ForeignKey(Benjamin, verbose_name="所属板块")
    owner = models.ForeignKey(User, verbose_name="作者")
    title = models.CharField(u"文章名", max_length=300)
    content = models.CharField(u"文章内容", max_length=10000)
    status = models.IntegerField(u"状态", choices=((0, u"普通"), (1, u"正常"), (10, u"精华")), default=0)
    creat_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = u"文章"
