# coding: utf-8
from django.contrib import admin
from models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("block", "article", "owner", "content", "status", "last_update_timestamp")
    list_filter = ("block", )
    searche_field = ("content", )

admin.site.register(Comment, CommentAdmin)
