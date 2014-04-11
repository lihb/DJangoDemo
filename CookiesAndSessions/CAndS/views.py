# coding:utf8

from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from CAndS.models import User


class regForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

def register(req):
	if req.method == 'POST':
		rf = regForm(req.POST)
		if rf.is_valid():
			username = rf.cleaned_data['username']
			password = rf.cleaned_data['password']
			User.objects.create(username=username, password=password)
			return  HttpResponseRedirect('/login')
	else:
		rf = regForm()
	return render_to_response('register.html',{'rf':rf})


def login(req):
	if req.method == 'POST':
		rf = regForm(req.POST)
		if rf.is_valid():
			username = rf.cleaned_data['username']
			password = rf.cleaned_data['password']
			users = User.objects.filter(username__exact=username, password__exact=password)
			if users:
				res = HttpResponseRedirect('/index')
				#res.set_cookie('username', username, 3600)  #cookie方式传递数据，数据存储在客户端浏览器中
				req.session['username'] = username           #session方式传递数据，数据存储在数据库中
				return res
			else :
				return HttpResponseRedirect('/login')
	else:
		rf = regForm()
	return render_to_response('login.html',{'rf':rf})



def index(req):
	#username = req.COOKIES.get('username','nobody')
	username = req.session.get('username', 'nobody')
	return render_to_response('index.html', {'username':username})




def logout(req):
	#response = HttpResponse('GoodBye')     #cookie方式
	#response.delete_cookie('username')     #cookie方式
	#return response                        #cookie方式
	del req.session['username']             #session方式
	return HttpResponse('GoodBye!')         #session方式





