from django.db import models

class User(models.Model):
   username = models.CharField(max_length=30)
   headImg  = models.FileField(upload_to='./Upload/uploadFiles/')
	
   def __unicode__(self):
	   return self.username
