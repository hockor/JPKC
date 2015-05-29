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
	isVideo = models.BooleanField(u"是否为视频",default = False)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u"上传"
		verbose_name_plural = u"上传"

class Announcement(models.Model):
	name = models.CharField(max_length = 30)
	content = models.TextField(u"内容")
	time = models.DateTimeField(u"时间",default = datetime.now)

	class Meta:
		verbose_name = u"公告"
		verbose_name_plural = u"公告"

class New(models.Model):
	name = models.CharField(max_length = 30)
	content = models.TextField(u"内容")
	time = models.DateTimeField(u"时间",default = datetime.now)

	class Meta:
		verbose_name = u"新闻"
		verbose_name_plural = u"新闻"

class Paper(models.Model):
	user = models.ForeignKey(User,null = True,blank = True)
	exam = models.CharField(u"试卷名称",max_length = 40)
	person = models.CharField(u"出题人",max_length = 20)
	totalscore = models.IntegerField(u"总分")
	time = models.DateTimeField(u"时间",default = datetime.now)
	flag = models.BooleanField(default = False)

	class Meta:
		verbose_name = u"试卷" 
		verbose_name_plural = u"试卷"

	def __unicode__(self):
		return self.exam


class Exam(models.Model):
	test = models.ForeignKey(Paper,related_name='试卷名称')
	question = models.TextField(u"题目")
	optionA = models.CharField(u"A",max_length = 200)
	optionB = models.CharField(u"B",max_length = 200)
	optionC = models.CharField(u"C",max_length = 200)
	optionD = models.CharField(u"D",max_length = 200)
	answer = models.CharField(u"答案",max_length = 2)
	score = models.IntegerField(u"分数")

	def __unicode__(self):
		return self.test.exam


	class Meta:
		verbose_name = u"试题"
		verbose_name_plural = u"试题"


class FinishExam(models.Model):
	user = models.ForeignKey(User)
	paper = models.ForeignKey(Paper)
	score = models.IntegerField()
	time = models.DateTimeField(default = datetime.now)

def wtFile(buf,name):
	fp = open(name,'wb')
	fp.write(buf)
	fp.close()
	cmd = 'chmod 777 ' + name
	os.system(cmd)
	setEvents(name)

@login_required
def uploadScript(request):
	file = request.FILES.get("Filedata",None)
	result,buf = profileUpload(file)
	wtFile(buf,file.name)
	return HttpResponse(simplejson.dumps({'message':'ok'}))