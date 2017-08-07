# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Article(models.Model):
    title = models.CharField(max_length =20)
    desc = models.CharField(max_length = 100)
    date_publish = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    user = models.ForeignKey(User)
    def __unicode__(self):
	return self.title
