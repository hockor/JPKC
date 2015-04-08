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

class UploadFile(models.Model):
	name = models.CharField(u"名称",max_length = 30)
	file = models.FileField(u"文件",upload_to = './upload/')

	def __unicode__(self):
		return self.name

class Announcement(models.Model):
	name = models.CharField(max_length = 30)
	content = models.TextField(u"内容")
	time = models.DateTimeField(u"时间",default = datetime.now)

class New(models.Model):
	name = models.CharField(max_length = 30)
	content = models.TextField(u"内容")
	time = models.DateTimeField(u"时间",default = datetime.now)

