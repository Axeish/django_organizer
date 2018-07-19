from django.db import models


class Entry(models.Model):
	name = models.CharField(max_length=200)
	type = models.CharField(max_length= 200)
	date = models.DateTimeField()
	description = models.TextField()

class States(Entry):	
	record = models.IntegerField()

# Create your models here.
