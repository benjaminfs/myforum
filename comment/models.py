# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from article.models import Article
from buluojianshe.models import Benjamin


class Comment(models.Model):
    block = models.ForeignKey(Benjamin, verbose_name=u'所属板块')
    article = models.ForeignKey(Article, verbose_name=u'所属文章')
    owner = models.ForeignKey(User, verbose_name=u'评论者')
    to_comment_id = models.IntegerField(u'回复评论', default=0)
    content = models.CharField(u'评论内容', max_length=2000)
    status = models.IntegerField(u'状态', choices=((0, u'普通'), (-1, u'删除')), default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    @property
    def to_comment(self):
        if not self.to_comment_id:
            return None
        else:
            return Comment.objects.get(id=self.to_comment_id)

    def __unicode__(self):
        return self.content[:20]

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'
