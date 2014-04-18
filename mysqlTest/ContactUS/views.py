#coding:utf8
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#version1--没有使用forms类
#def contact(req):
#	errors=[]
#	if req.method == 'POST':
#		if not req.POST.get('subject', ''):
#			errors.append('Enter a subject.')
#		if not req.POST.get('message', ''):
#			errors.append('Enter a message.')
#		if not req.POST.get('email', '') and '@' not in req.POST('email'):
#			errors.append('Enter a valid e-mail address.')
#		if not errors:
#			send_mail(
#					req.POST['subject'],
#					req.POST['message'],
#					req.POST.get('email', 'noreply@example.com'),
#					['siteowner@example.com'],
#			)
#			return HttpResponseRedirect('/contact/thanks')
#	return render_to_response('contact_form.html', {'errors':errors})

# version2--使用formes类
from ContactUS.forms import ContactForm
def contact(req):
	if req.method == "POST":
		cform = ContactForm(req.POST)
		if cform.is_valid():
			data = cform.cleaned_data
			send_mail(
				data['subject'],
				data['message'],
				data.get('email', 'noreply@example.com'),
				['siteowner@example.com',],
			)
			req.session['subject'] = data['subject']
			req.session['message'] = data['message']
			req.session['email'] = data.get('email','noreply@example.com')

			return HttpResponseRedirect('/contact/thanks/')
	else:
		cform = ContactForm(
			initial = {'subject':'I love your site.', 'message':'haha', 'email':'xxx@xxx.com'}  # initial参数--设置初始值		
		)
	return render_to_response('contact_form.html',{'cform':cform})
			



def thanks(req):
	info = req.session
	return render_to_response('thanks.html', {'info':info})
