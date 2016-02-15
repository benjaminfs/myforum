#  coding: utf-8
from django.contrib import admin
from models import Benjamin


class BenjaminAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager", "creat_timestamp", "last_update_timestamp")
    #  list_filter = (u"时间", "creat_timestamp")
    list_filter = ("creat_timestamp", "last_update_timestamp", "name")

admin.site.register(Benjamin, BenjaminAdmin)
