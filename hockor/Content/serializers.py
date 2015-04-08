#!/usr/bin/env python
#-*-coding:utf8-*-

from Content.models import Announcement,New
from rest_framework import serializers

class AnnouncementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Announcement
		fields = ('name','content','time')

class NewSerializer(serializers.ModelSerializer):
	class Meta:
		model = New
		fields = ('name','content','time')

