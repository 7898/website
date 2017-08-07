# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc')
    class Media:
        js = (
             '/static/js/kindeditor-4.1.10/kindeditor-min.js',
             '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
             '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(User)
admin.site.register(Article,ArticleAdmin)
