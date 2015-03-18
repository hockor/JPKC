#!/usr/bin/env python
#-*-coding:utf8-*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()
import hockor.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hockor.views.home', name='home'),
    # url(r'^hockor/', include('hockor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^$','hockor.views.logoHd'),
    url(r'^home/$','hockor.views.HomeHd'),
    url(r'^register/$','User.views.RegisterHd'),
    url(r'^login/$','User.views.LoginHd'),
    url(r'^logout/$','User.views.LogoutHd'),
)
