from django.shortcuts import render_to_response
from models import Benjamin


def buluojianshe_list(request):
    benjamins = Benjamin.objects.all().order_by("-id")
    return render_to_response("buluojianshe_list.html", {"benjamins": benjamins})
