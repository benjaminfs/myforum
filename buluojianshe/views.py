from django.shortcuts import render_to_response
from models import Benjamin
from django.template import RequestContext
from message.models import UserMessage


def buluojianshe_list(request):
    if request.user.is_authenticated():
        msg_cnt = UserMessage.objects.filter(owner=request.user, status=0).count()
    else:
        msg_cnt = 0
    benjamins = Benjamin.objects.all().order_by("-id")
    return render_to_response("buluojianshe_list.html", {"benjamins": benjamins, "msg_cnt": msg_cnt}, context_instance=RequestContext(request))
