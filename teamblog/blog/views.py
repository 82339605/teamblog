
import datetime
from django.core import serializers
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index_views(request):
    user=[]
    if 'uid' in request.session and 'uname' in request.session:
        user = User.objects.get(id=request.session['uid'])
    message = Message.objects.all()
    topic = Topic.objects.all()
    return render(request,'blog.html',locals())
def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        del request.session['uname']
    return redirect(request.META.get('HTTP_REFERER','/'))
def register(request):
    if request.method == "POST":
        loginname = request.POST['login']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        url = request.POST['url']
        user = User()
        user.username = username
        user.loginname = loginname
        user.uemail = email
        user.pwd = password
        user.url = url
        user.save()
        request.session['uid'] = user.id
        request.session['uname'] = user.username
        return redirect('/')
    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'GET':
        request.COOKIES['url'] = request.META.get('HTTP_REFERER','/')
        url = request.COOKIES.get('url','/')
        if 'uname' in request.session and 'uid' in request.session:
            return redirect(url)
        return render(request,'login.html')
    else:
        uname = request.POST['username']
        pwd = request.POST['password']
        information = User.objects.filter(username=uname, pwd=pwd)
        if information:
            request.session['uname'] = uname
            request.session['uid'] = information[0].id
            url = request.COOKIES.get('url','/')
            resp = redirect(url)
            if 'url' in request.COOKIES:
                resp.delete_cookie('url')
            return resp
        else:
            return render(request,'login.html')
def check(request):
    uname = request.GET['uname']
    print(uname)
    if User.objects.filter(username=uname):
        # 判断是否已被注册，并且返回相应的内容
        message = '此用户名已被注册'
        status = 0
    else:
        message = '合法用户名'
        status = 1
    dic = {
    'msg':message,
    'status':status}
    dic = json.dumps(dic)
    #返回字典，并且前端通过status去判断该返回什么值
    return HttpResponse(dic)
def publish(request):
    if request.method == "GET":
        if 'uid' in request.session and 'uname' in request.session and request.session['uid'] == 1:
            return render(request,'publish.html')
        else:
            return redirect('/')
    else:
        topic = Topic()
        justOne = request.POST['justOne']
        title = request.POST['title']
        select = request.POST['select']
        message = request.POST['message']
        if request.FILES.get('file'):
            file = request.FILES['file']
            filename = request.FILES['file'].name
            exc = filename.split('.')[1]
            time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            file.filename = time+'.'+exc
            topic.imgs = file
        topic.justOne = justOne
        topic.title = title
        topic.select = select
        topic.content = message
        topic.save()
        return redirect('/')
def info(request):
    msg = Message.objects.all()
    first = msg[0]
    third = msg[2]
    return render(request,'info.html',locals())
def info2(request):
    msg = Message.objects.all()
    second = msg[1]
    return render(request,'info2.html',locals())
def info3(request):
    msg = Message.objects.all()
    third = msg[2]
    return render(request,'info3.html',locals())
def leave(request):
    if request.method=="GET":
        return  render(request,'leave.html')
    else:
        text = request.POST['text']
        name = request.POST['number']
        msg = aboutMy()
        msg.name = name
        msg.text = text
        msg.save()
        return redirect('/')
def text(request):
    return render(request,'text.html')
def aboutmy(request):
    if 'uid' in request.session and 'uname' in request.session and request.session['uid'] == 1:
        info = aboutMy.objects.all()
        return render(request, 'aboutMy.html', locals())
    else:
        return redirect('/')
def note(request):
    return render(request,'note.html')
def note1(request):
    return render(request,'note1.html')
def note2(request):
    return render(request,'note2.html')
def note3(request):
    return render(request,'note3.html')
def time(request):
    return render(request,'time.html')
def luanting(request):
    return render(request,'luanting.html')
def tarena(request):
    return render(request,'tarena.html')
def checkPow(request):
    if 'uid' in request.session and 'uname' in request.session and request.session['uid'] == 1:
        dic = {
            'stu':1,
        }
        return HttpResponse(json.dumps(dic))
    dic = {
        'stu':0,
        'msge':'抱歉，非本博主不可发表博客',
        }
    return HttpResponse(json.dumps(dic))
def about(request):
    return render(request,'about.html')
