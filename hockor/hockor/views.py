#!/usr/bin/rnv python
#-*-coding:utf8-*-

from django.http import HttpResponse
from django.template import RequestContext,loader

	
def HomeHd(request):
	template = loader.get_template('home.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))