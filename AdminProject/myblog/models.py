from django.db import models

sex_choice = (
		('m', 'male'),
		('f', 'female'),
)
class User(models.Model):
	name = models.CharField(max_length=20)
	sex = models.CharField(max_length=1, choices=sex_choice)
	age = models.CharField(max_length=10)

	def __unicode__(self):
		return '%s %s %s ' % (self.name, self.sex, self.age)
