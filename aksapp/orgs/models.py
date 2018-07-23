from django.db import models


class Entry(models.Model):
	name = models.CharField(max_length=200)
	type = models.CharField(max_length= 200)
	date = models.DateTimeField(auto_now= False, auto_now_add=True)
	updated = models.DateTimeField(auto_now= True, auto_now_add= False)
	description = models.TextField()

class States(Entry):	
	record = models.IntegerField()

# Create your models here.
