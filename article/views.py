# coding:utf-8
from django.shortcuts import render_to_response, redirect
from buluojianshe.models import Benjamin
from models import Article
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.urlresolvers import reverse


def article_list(request, block_id):
        block_id = int(block_id)
        block = Benjamin.objects.get(id=block_id)
        articles = Article.objects.filter(block=block).order_by("last_update_timestamp")
        return render_to_response("article_list.html", {"articles": articles, "buluojianshe": block}, context_instance=RequestContext(request))


# 创建文章
def article_create(request, block_id):
    block_id = int(block_id)
    block = Benjamin.objects.get(id=block_id)
    if request.method == "GET":
        return render_to_response("article_create.html", {"buluojianshe": block}, context_instance=RequestContext(request))
    elif request.method == "POST":
        title = request.POST['title'].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request, messages.ERROR, u"标题与内容均不能为空")
            return render_to_response("article_create.html", {"buluojianshe": block, "title": title, "content": content}, context_instance=RequestContext(request))
        owner = User.objects.all()[0]
        new_article = Article(block=block, owner=owner, title=title, content=content)
        new_article.save()
        messages.add_message(request, messages.INFO, u"文章发表成功")
        return redirect(reverse("article_list", args=[block.id]))


def article_detail(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    return render_to_response("article_detail.html", {"article": article}, context_instance=RequestContext(request))
