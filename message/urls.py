from django.conf.urls import url


urlpatterns = [
        url(r'^list/$', "message.views.message_list", name="message_list"),
        url(r'^read/(?P<message_id>\d+)$', "message.views.message_read", name="read_message"),
]
