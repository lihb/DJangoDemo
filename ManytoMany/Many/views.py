from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Many.models import Author, Book

def show_author(req):
	authors = Author.objects.all()
	return render_to_response('show_author.html', {'authors':authors})

def show_book(req):
	books = Book.objects.all()
	return render_to_response('show_book.html', {'books':books})

class UserForm(forms.Form):
	name = forms.CharField()
	age = forms.CharField()

def register(req):
	if req.method == 'POST':
		form = UserForm(req.POST)
		if form.is_valid():
			data =  form.cleaned_data 
			print data
			return HttpResponse('name = '+data['name']+' , age = '+data['age'])
	else:
		form = UserForm()
	return render_to_response('register.html', {'form':form})

sex_choice = (
      ('F','female'),
	  ('M','male'),
)

class UploadForm(forms.Form):
	name = forms.CharField()
	sex = forms.ChoiceField(choices = sex_choice)
	file = forms.FileField()

def regist(req):
	if req.method =='POST':
		uploadform = UploadForm(req.POST, req.FILES)
		if uploadform.is_valid():
			data = uploadform.cleaned_data['file']
			print data
			with open('/home/lhb/upload/' + data.name, 'wb+') as dest:
				for chunk in data.chunks():
					dest.write(chunk)
			return HttpResponse('OK')
	else:
		uploadform = UploadForm()
	return render_to_response('regist.html', {'uploadform':uploadform})
