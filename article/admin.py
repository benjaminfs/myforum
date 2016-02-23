#  coding:utf-8
from django.contrib import admin
from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block", "owner", "title", "content", "status")
    serch_fields = ["title", "content"]
    list_filter = ("owner", "status")

admin.site.register(Article, ArticleAdmin)
