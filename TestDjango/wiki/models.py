from django.db import models

class Person(models.Model):
	
	name = models.CharField(max_length = 20, unique = True)
	sex = models.CharField(max_length = 10)
	age = models.CharField(max_length = 10)

	def __unicode__(self):
		return self.name

class Dept(models.Model):
	name = models.CharField(max_length = 20, unique = True)
	leader = models.ForeignKey(Person)
	
	def __unicode__(self):
		return self.name


