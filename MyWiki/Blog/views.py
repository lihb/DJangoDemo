# coding:utf8

import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django import forms
from Blog.blogforms import UserForm, BlogForm, LoginForm
from Blog.models import User, Blog



def register(req):
	if req.method == 'POST':
		userForm = UserForm(req.POST)
		if userForm.is_valid():
			infos = userForm.cleaned_data
			username = infos['username']
			password = infos['password']
			sex = infos['sex']
			email = infos['email']
			User.objects.create(username = username, password = password, sex = sex, email = email)
			return HttpResponseRedirect('login')
	else:
		userForm = UserForm()
	return render_to_response('register.html', {'userForm':userForm}, context_instance=RequestContext(req))

def login(req):
	if req.method == 'POST':
		loginForm = LoginForm(req.POST)
		if loginForm.is_valid():
			infos = loginForm.cleaned_data
			username = infos['username']
			password = infos['password']
			user = User.objects.filter(username__exact = username, password__exact = password)
			if user:
				return HttpResponseRedirect('index')
	else:
		loginForm = LoginForm()
	return render_to_response('login.html', {'loginForm':loginForm}, context_instance=RequestContext(req))


def index(req):
	blogs = Blog.objects.all()
	return render_to_response('index.html', {'blogs':blogs})


def add(req):
	if req.method == 'POST':
		blogForm = BlogForm(req.POST)
		if blogForm.is_valid():
			infos = blogForm.cleaned_data
			title = infos['title']
			content = infos['content']
			author = infos['author']
			post_date = datetime.datetime.now()
			
			blog = Blog()
			blog.title = title
			blog.author = author
			blog.content = content
			blog.post_date = post_date
			blog.save()
			return HttpResponseRedirect('index')
	else:
		blogForm = BlogForm()
	return render_to_response('add.html', {'blogForm':blogForm}, context_instance=RequestContext(req))



def show(req):
	if 'title' in req.GET:
		title = req.GET["title"]
		blog  = Blog.objects.get(title = title)
		return render_to_response('show.html', {'blog':blog})
	else:
		return render_to_response('index.html', {})

def modify(req):
	if req.method == 'GET':
		if 'title' in req.GET:
			title = req.GET["title"]
			blog  = Blog.objects.get(title = title)
			blog.delete()
		else:
			return render_to_response('index.html', {})
	if req.method == 'POST':
		blogForm = BlogForm(req.POST)
		if blogForm.is_valid():
			infos = blogForm.cleaned_data
			title = infos['title']
			content = infos['content']
			author = infos['author']
			post_date = datetime.datetime.now()
			
			blog = Blog()
			blog.title = title
			blog.author = author
			blog.content = content
			blog.post_date = post_date
			blog.save()
			return HttpResponseRedirect('index')
	else:
		blogForm = BlogForm()
	return render_to_response('modify.html', {'blogForm':blogForm}, context_instance=RequestContext(req))


def delete(req):
	msg =''
	if req.method == 'GET':
		if 'title' in req.GET:
			title = req.GET["title"]
			blog  = Blog.objects.get(title = title)
			blog.delete()
			msg = '删除成功'
		
	return render_to_response('delete.html', {'msg':msg})



