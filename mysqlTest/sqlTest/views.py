#coding:utf8

from django.shortcuts import render_to_response
from django.http import HttpResponse
from sqlTest.models import Book

def display_request(req):
	path = req.path
	host = req.get_host()

	meta_info = req.META

	return render_to_response('display.html', {'path':path, 'host':host, 'meta_info':meta_info})
	
def search_form(req):
	return render_to_response('search_form.html')

def search(req):
	error = False
	if 'q' in req.GET:
		q = req.GET['q']
		if not q:
			error = True
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_result.html', {'books':books, 'query':q}) # 处理数据，结果可能包含多条数据也可能没有数据，放在html页面处理（想想为什么）
	return render_to_response('search_form.html', {'error':error})  # 处理空字符串

