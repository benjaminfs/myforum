from django.contrib import admin
from models import benjamin


class benjaminAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_num", "sex", "owner", "last_update_timestamp")
    list_filter = ("sex", )

admin.site.register(benjamin, benjaminAdmin)
