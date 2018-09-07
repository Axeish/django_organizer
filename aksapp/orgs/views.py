from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Entry
from .forms import EntryForm, TodoForm
from .today import Today
from .astro import speak_gemini
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView
from django.views.decorators.http import require_POST
from .models import Task
import datetime


# Create your views here.

from .models import Entry

def index(request):
    entries = Entry.objects.all().order_by("-date")
    query= request.GET.get('q')
    if query:
        entries = entries.filter(type__icontains=query) 
        print(entries)
        print(len(entries))
    paginator = Paginator(entries, 15)
    page = request.GET.get('page')  
    try:
        entries_set = paginator.page(page)
    except PageNotAnInteger:
        entries_set = paginator.page(1)
    except EmptyPage:
        entries_set = paginator.page(  paginator.num_pages)      
    return render(request, "posts.html", {'entries': entries_set})
    

def today(request):
    tasks = Task.objects.all().order_by("-date")
    todoform = TodoForm()
    now = Today()
    stre = speak_gemini("www.astrospeak.com/horoscope/gemini")
    strnow = now.date
    day = now.day
    th ="th"
    if now.position <3:
        if now.position == 1:
            th = "st"
        else:
            th = "nd"
    th = str(now.position) + th        
    entries = Entry.objects.all().order_by("-date")
    query= request.GET.get('q')
    if query:
        entries = entries.filter(type__icontains=query) 
        print(entries)
        print(len(entries))
    paginator = Paginator(entries, 15)
    page = request.GET.get('page')  
    try:
        entries_set = paginator.page(page)
    except PageNotAnInteger:
        entries_set = paginator.page(1)
    except EmptyPage:
        entries_set = paginator.page(  paginator.num_pages)
    context = {'entries': entries_set, 'date' : strnow, 'th': th, 'day':day, 'tasks': tasks, 'stre': stre, 'todoform' : todoform }          
    return render(request, "index.html", context)
    

@require_POST
def addtodo(request):
    form = TodoForm(request.POST)
    print(request.POST['name'])
    if form.is_valid():
        new_todo = Task(name=request.POST['name'])
        new_todo.save()
    return redirect('today')   

def completetodo(request, todo_id):
    todo = Task.objects.get(pk=todo_id)
    todo.done = True
    todo.save()
    return redirect('today') 

def deletecomplete(request):
    Task.objects.filter(done__exact=True).delete()
    return redirect('today') 

def deleteone(request,todo_id):
    todo = get_object_or_404(Task,pk=todo_id)
    todo.delete()
    return redirect('today') 

def details(request,pk):
	entry = Entry.objects.get(id=pk)
	return render(request, "details.html", {'entry':entry})


def delete(request,pk):
	if request.method == 'DELETE':
	    entry = get_object_or_404(Entry,pk=pk)
	    entry.delete()
	return HttpResponseRedirect('/')

def update(request,pk):
    instance = get_object_or_404(Entry,pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST or None,instance=instance )
        if form.is_valid():
            instance =form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')      
    else:
        form = EntryForm(instance=instance )

    return render(request, "form.html", {"name":instance.name,'instance':instance,'form': form})

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')      
    else:
        form = EntryForm()

    return render(request, "form.html", {'form': form})
