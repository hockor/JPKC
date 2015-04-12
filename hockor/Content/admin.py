#!/usr/bin/env python
#-*-coding:utf8-*-

from django.contrib import admin
from Content.models import UploadFile,Announcement,New

class Announcemment(admin.ModelAdmin):
	list_display = ('name','content','time')

class NewAdmin(admin.ModelAdmin):
	list_display =  ('name','content','time')

admin.site.register(UploadFile)
admin.site.register(Announcement)
admin.site.register(New)
