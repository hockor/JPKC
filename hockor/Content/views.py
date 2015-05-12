#-*-coding:utf8-*-

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,loader
from django.shortcuts import render
from django.utils import simplejson
from User.models import *
from Content.models import *
from Content.serializers import AnnouncementSerializer,NewSerializer,ExamSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def SubjectHd(request):
	videos = UploadFile.objects.filter(isVideo = True)
	template = loader.get_template('content/subject.html')
	context = RequestContext(request,{'videos':videos})
	return HttpResponse(template.render(context))

def AboutHd(request):
	template = loader.get_template('content/about.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def FileHd(request):
	files = UploadFile.objects.filter(isVideo = False)
	template = loader.get_template('content/file.html')
	context = RequestContext(request,{'files':files})
	return HttpResponse(template.render(context))

def MessageHd(request):
	template = loader.get_template('content/message.html')
	message = Message.objects.all()
	backmessage = BackMessage.objects.all()
	context = RequestContext(request,{'message':message,'backmessage':backmessage})
	return HttpResponse(template.render(context))

def TestHd(request):
	tests = Paper.objects.all()
	getscores = FinishExam.objects.filter(user_id = request.user.id)
	template = loader.get_template('content/test.html')
	context = RequestContext(request,{'tests':tests,'getscores':getscores})
	return HttpResponse(template.render(context))

def NewTestHd(request):
	tests = Paper.objects.all()
	template = loader.get_template('content/newtest.html')
	context = RequestContext(request,{'tests':tests})
	return HttpResponse(template.render(context))

def ComplateTestHd(request):
	template = loader.get_template('content/complatetest.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def stMsg(username,message):
	try:
		obj = Message(name = username,message = message)
		obj.save()
		return True
	except:
		return False

def getMessage(request):
	if request.method != 'post' or not request.is_ajax():
		raise Http404
	message = request.POST.get("message")
	if stMsg(request.user.username,message):
		return HttpResponse(simplejson.dumps({'message':'ok'}))
	else:
		return HttpResponse(simplejson.dumps({'message':'error'}))

def stBackMsg(msgid,contents):
	try:
		obj = BackMessage(msg_id = msgid,contents = contents)
		obj.save()
		return True
	except:
		return False

def backMessage(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	msgid = request.POST.get("id")
	contents = request.POST.get("contents")
	if stBackMsg(msgid,contents):
		return HttpResponse(simplejson.dumps({'message':'ok'}))
	else:
		return HttpResponse(simplejson.dumps({'message':'error'}))

class AnnouncementList(APIView):
	def get(self,request,format=None):
		announcements = Announcement.objects.all()
		serializer = AnnouncementSerializer(announcements,many = True)
		return Response({'status':200,'data':serializer.data})

class NewList(APIView):
	def get(self,request,format=None):
		news = New.objects.all()
		serializer = NewSerializer(news,many = True)
		return Response({'status':200,'data':serializer.data})


class ExamDetail(APIView):
	def get(self,request,pk,format = None):
		exams = Exam.objects.filter(test_id = pk)
		serializer = ExamSerializer(exams,many = True)
		return Response({'status':200,'data':serializer.data})

	def post_data(self,answer,id):
		exam = Exam.objects.filter(test_id = id)
		score = 0
		test  = []
		for i in range(len(exam)):
			if exam[i].answer == answer[i]:
				score = score + exam[i].score
				test.append('Y')
			else:
				test.append('N')
		return score,test

	def post_exam(self,score,pk,user):
		if FinishExam.objects.filter(user_id = user.id,paper_id = pk).count()>0:
			obj = FinishExam.objects.get(user_id = user.id,paper_id = pk)
			obj.score = score
			obj.time = datetime.now()
			obj.save()
		else:
			op = FinishExam(user_id = user.id,paper_id = pk,score = score)
			op.save()

	def post(self,request,pk,format = None):
		try:
			answer = simplejson.loads(request.data['answer'])
			score,test = self.post_data(answer,pk)
			self.post_exam(score,pk,request.user)
			return Response({'status':0,'score':score,'test':test})
		except:
			return Response({'status':1})

def getAnswer(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	id = request.POST.get("id")
	answer = request.POST.get("answer")
	try:
		obj = Exam.objects.get(id = id)
		if obj.answer == answer:
			return HttpResponse(simplejson.dumps({'score':obj.score}))
		else:
			return HttpResponse(simplejson.dumps({'score':0}))
	except:
		return HttpResponse(simplejson.dumps({'score':'error'}))

def getAllScore(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	score = request.POST.get('score')
	paperid = request.POST.get('paperid')
	try:
		obj = FinishExam(user_id = request.user.id,paper_id = paperid,score = score)
		obj.save()
		return HttpResponse(simplejson.dumps({'score':score}))
	except:
		return HttpResponse(simplejson.dumps({'score':'error'}))

def readfile(name):
	name = 'hockor/media/upload/' + name
	fp = open(name,'rb')
	buf = fp.read()
	fp.close()
	return buf

def downLoad(request,sid):
	try:
		obj = UploadFile.objects.get(id = sid)
		name = str(obj.file)
		name = name.split('/')[-1]
		buf = readfile(name)
		response = HttpResponse(buf,mimetype = 'application/octet-stream')
		response['Content-Disposition'] = 'attachment;filename=%s' % name
		return response
	except:
		raise Http404

def getVideo(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	id = request.POST.get('id')
	try:
		op = UploadFile.objects.get(id = id)
		path = op.file
		return HttpResponse(simplejson.dumps({'message':path}))
	except:
		return HttpResponse(simplejson.dumps({'message':'error'}))
