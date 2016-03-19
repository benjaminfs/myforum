from django.shortcuts import render_to_response
from models import Benjamin
from django.template import RequestContext


def buluojianshe_list(request):
    benjamins = Benjamin.objects.all().order_by("-id")
    return render_to_response("buluojianshe_list.html", {"benjamins": benjamins}, context_instance=RequestContext(request))
