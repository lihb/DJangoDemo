from django.shortcuts import render_to_response

title = "lhb's websitie"
info={'name':'lhb','age':100, 'sex':'male', 'address':'Guangdong Guangzhou', 'School':'SCNU'}

def index(request):
	return render_to_response('index.html', {'information':info, 'title':title})
