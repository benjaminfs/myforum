from django.conf.urls import url


urlpatterns = [
        url(r'^register$', "usercenter.views.register", name="usercenter_register"),
        url(r'^login/$', "usercenter.views.login", name="user_login"),
        url(r'^logout/$', "django.contrib.auth.views.logout_then_login", name="user_logout"),
        url(r'^activate/(?P<code>\w+)$', "usercenter.views.activate", name="usercenter_activate"),
]
