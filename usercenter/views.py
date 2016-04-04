# coding:utf-8
import datetime
import uuid

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from models import ActivateCode


# 用户注册
def register(request):
    error = ""
    if request.method == "GET":
        return render_to_response("usercenter_register.html", {}, context_instance=RequestContext(request))
    else:
        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        password = request.POST["password"].strip()
        re_password = request.POST["re_password"].strip()
        if not username or not password or not email:
            error = u"用户名，密码，邮箱均不能为空"
        if password != re_password:
            error = u"两次密码不一致"
        if User.objects.filter(username=username).count() > 0:
            error = u"用户名已经存在"
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()

            new_code = str(uuid.uuid4()).replace("-", "")
            expire_time = datetime.datetime.now() + datetime.timedelta(days=2)
            code_record = ActivateCode(owner=user, code=new_code, expire_timestamp=expire_time)
            code_record.save()

            activate_link = "http://%s%s" % (request.get_host(), reverse("usercenter_activate", args=[new_code]))
            send_mail(u'benjamin激活邮件', u'点击链接进行激活: %s' % activate_link, "h1n1china@163.com", [email], fail_silently=False)
        else:
            return render_to_response("usercenter_register.html", {"error": error}, context_instance=RequestContext(request))
        return redirect(reverse("login"))


# 激活用户
def activate(request, code):
    query = ActivateCode.objects.filter(code=code, expire_timestamp__gte=datetime.datetime.now())
    if query.count() > 0:
        code_record = query[0]
        code_record.owner.is_active = True
        code_record.owner.save()
        return HttpResponse(u"激活成功")
    else:
        return HttpResponse(u"激活失败")


# 用户登录
def user_login(request):
    error = []
    if request.method == 'GET':
        return render_to_response("login.html", {}, context_instance=RequestContext(request))
    else:
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        user = authenticate(username=username, password=password)
    if not username or not password:
        error.append(u"用户名或密码必须填写")
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response("buluojianshe_list.html", {}, context_response=RequestContext(request))
            else:
                error.append(u"用户未激活")
        else:
            error.append(u"用户名或密码错误")
            return render_to_response("login.html", {"error": error}, context_response=RequestContext(request))
        return redirect(reverse("login.html"))


# 用户退出
def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return render_to_response("buluojianshe_list.html", {}, context_response=RequestContext(request))
    return redirect(reverse("buluojianshe_list.html"))
