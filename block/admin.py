from django.contrib import admin
from models import Demo


class DemoAdmin(admin.ModelAdmin):
    list_display = ("example4char", "example4int", "sex", "owner", "last_update_timestamp")
    list_filter = ("sex", )

admin.site.register(Demo, DemoAdmin)
