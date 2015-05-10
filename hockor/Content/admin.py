#!/usr/bin/env python
#-*-coding:utf8-*-

from django.contrib import admin
from Content.models import UploadFile,Announcement,New,Paper,Exam

class UploadFileAdmin(admin.ModelAdmin):
	list_display = ['name','isVideo']

class AnnouncemmentAdmin(admin.ModelAdmin):
	list_display = ['name','content','time']

class NewAdmin(admin.ModelAdmin):
	list_display =  ['name','content','time']



class ExamAdmin(admin.ModelAdmin):
	list_display = ['question','optionA','optionB','optionC','optionD','answer','score']
	list_display_links = ['question']
	search_fields = ['question']

class PaperAdmin(admin.ModelAdmin):
	date_hierarchy = 'time'
	list_display = ['exam','person','totalscore','time']
	ordering = ['-id']
	list_display_links = ['exam']
	search_fields = ['exam','user__username','person']


admin.site.register(UploadFile,UploadFileAdmin)
admin.site.register(Announcement,AnnouncemmentAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Paper,PaperAdmin)
admin.site.register(Exam,ExamAdmin)
