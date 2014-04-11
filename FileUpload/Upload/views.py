from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse
from Upload.models import User


class UserForm(forms.Form):
	username = forms.CharField(max_length=30)
	headImg = forms.FileField()

def register(req):
	if req.method=='POST':
		uf = UserForm(req.POST, req.FILES)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			headImg  = uf.cleaned_data['headImg']
			print username, headImg
			user  = User()
			user.username = username
			user.headImg = headImg
			user.save()
			return HttpResponse('OK')
	else:
		uf = UserForm()
	return render_to_response('register.html', {'uf':uf})


