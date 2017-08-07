# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import *
# Create your views here.

def global_setting(request):
    SITE_TITLE = 'NOTEBOOK'
    SITE_DESC = 'STAY HUNGRY. STAY FOOLISH.'
    return locals()


def index(request):
    article_list = Article.objects.all()
    return render(request,'index.html',locals())

def article(request):
    article_id = request.GET.get('id',None)
    try:
	article = Article.objects.get(id = article_id)
    except:
	return render(request,'failure.html',{reason:'sorry,not find this page'})
    return render(request,'article.html',locals())
