from django.db import models


sex_choice = (
	('F', 'Female'),
	('M','Male'),
)


class User(models.Model):
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50)
	sex  = models.CharField(max_length=10, choices = sex_choice, default = 'F')
	email =models.EmailField(max_length=75)

	def __unicode__(self):
		return self.username

	class Meta:
		ordering = ['username']



class Blog(models.Model):
	title = models.CharField(max_length=50,unique=True)
	author = models.ForeignKey(User)
	content = models.CharField(max_length=2000)
	post_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-post_date']



