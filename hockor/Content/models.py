#/usr/bin/ python
#-*-coding:utf8-*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Message(models.Model):
	name = models.CharField(max_length = 50)
	message = models.CharField(max_length = 250,default = '')
	time = models.DateTimeField(default = datetime.now)

class BackMessage(models.Model):
	msg = models.ForeignKey(Message)
	contents = models.CharField(max_length = 250,default = '')
	time = models.DateTimeField(default = datetime.now)
