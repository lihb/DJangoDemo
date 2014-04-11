from django.shortcuts import render_to_response
from models import Person,Dept

def wiki_index(req):
	persons = Person.objects.all()
	return render_to_response('wikiIndex.html', {'persons':persons})

def manyToOne(req):
	dept = Dept.objects.all()
	return render_to_response("manyToOne.html", {'dept':dept})
