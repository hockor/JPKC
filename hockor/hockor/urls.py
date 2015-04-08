#!/usr/bin/env python
#-*-coding:utf8-*-
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
'''
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()
'''
import hockor.views
import settings
from Content import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hockor.views.home', name='home'),
    # url(r'^hockor/', include('hockor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','hockor.views.HomeHd'),
    url(r'^register/$','User.views.RegisterHd'),
    url(r'^login/$','User.views.LoginHd'),
    url(r'^logout/$','User.views.LogoutHd'),
    url(r'^loginhd/$','User.views.Login'),
    url(r'^about/$','Content.views.AboutHd'),
    url(r'^file/$','Content.views.FileHd'),
    url(r'^message/$','Content.views.MessageHd'),
    url(r'^subject/$','Content.views.SubjectHd'),
    url(r'^test/$','Content.views.TestHd'),
    url(r'^getmessage/$','Content.views.getMessage'),
    url(r'^backmessage/$','Content.views.backMessage'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^announcementlist/$',views.AnnouncementList.as_view()),
    url(r'^newlist/$',views.NewList.as_view()),
)


urlpatterns = format_suffix_patterns(urlpatterns)
