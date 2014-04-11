from django.shortcuts import render_to_response
from myblog.models import User

def index(req):
	users = User.objects.all()
	return  render_to_response('index.html', {'users':users})

