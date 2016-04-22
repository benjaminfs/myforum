# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from buluojianshe.models import Benjamin
from models import Article
from django.contrib import messages
# from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator


def article_list(request, block_id):
        block_id = int(block_id)
        block = Benjamin.objects.get(id=block_id)
        page_no = int(request.GET.get("page_no", "1"))
        articles = Article.objects.filter(block=block).order_by("last_update_timestamp")

        p = Paginator(articles, 1)
        if page_no > p.num_pages:
            page_no = p.num_pages
        if page_no <= 0:
            page_no = 1
        page_links = [i for i in range(page_no - 3, page_no + 5) if i > 0 and i <= p.num_pages]
        page = p.page(page_no)
        previous_link = page_links[0] - 1
        next_link = page_links[-1] + 1

        return render_to_response("article_list.html",
                                {"articles": page.articles, "buluojianshe": block,
                                "has_previous": previous_link > 0, "has_next": next_link <= p.num_pages,
                                "previous_link": previous_link,
                                "next_link": next_link,
                                "page_cnt": p.num_pages,
                                "current_no": page_no,
                                "page_links": page_links},
                                 context_instance=RequestContext(request))


# 创建文章
@login_required
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
# owner = User.objects.all()[0]
# owner=request.user
        new_article = Article(block=block, owner=request.user, title=title, content=content)
        new_article.save()
        messages.add_message(request, messages.INFO, u"文章发表成功")
        return redirect(reverse("article_list", args=[block.id]))


def article_detail(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    return render_to_response("article_detail.html", {"article": article}, context_instance=RequestContext(request))
