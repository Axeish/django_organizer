from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Entry
from .forms import EntryForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView
# Create your views here.

from .models import Entry

def index(request):
	entries = Entry.objects.all()
	return render(request, "index.html", {'entries': entries})

def today(request):
    entries = Entry.objects.all()
    query= request.GET.get('q')
    if query:
        entries = entries.filter(type__icontains=query) 
        print(entries)
        print(len(entries))
    paginator = Paginator(entries, 5)
    page = request.GET.get('page')  
    try:
        entries_set = paginator.page(page)
    except PageNotAnInteger:
        entries_set = paginator.page(1)
    except EmptyPage:
        entries_set = paginator.page(  paginator.num_pages)      
    return render(request, "index.html", {'entries': entries_set})
    

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
