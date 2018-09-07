from django.db import models


class Entry(models.Model):
	name = models.CharField(max_length=200)
	type = models.CharField(max_length= 200)
	date = models.DateTimeField(auto_now= False, auto_now_add=True)
	updated = models.DateTimeField(auto_now= True, auto_now_add= False)
	description = models.TextField()

class States(Entry):	
	record = models.IntegerField()

class Friends(models.Model):
	name = models.CharField(max_length=200)	
	record = models.IntegerField()

class Task(models.Model):
	name = models.CharField(max_length=200)
	done = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now= False, auto_now_add=True)
	
	

class SubTask(models.Model):
	task = models.ForeignKey('Task',on_delete=models.PROTECT)
	name = models.CharField(max_length=200)
	done = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now= False, auto_now_add=True)


class Fintask(models.Model):
	name = models.CharField(max_length=200)
	value =  models.FloatField()
	date = models.DateTimeField(auto_now= False, auto_now_add=True)
	