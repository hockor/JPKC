#!/usr/bin/env python
#-*-coding:utf8-*-

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	num = models.IntegerField()
	professional = models.CharField(max_length = 30)
	#img = models.ImageField()

	def __unicode__(self):
		return self.professional


def CreateUser(username,password,email,num,professional):
	user = User(username = username,email = email)
	user.set_password(password)
	user.is_staff = False
	user.save()

	profile = UserProfile(user = user,num = num,professional = professional)
	profile.save()
