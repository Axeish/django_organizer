"""aksapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from orgs import views

urlpatterns = [
    path('', views.today, name="today"),
    path('toadd', views.addtodo, name="toadd"),
    path('tocomplete/<todo_id>', views.completetodo, name="tocomplete"),
    path('todelc', views.deletecomplete, name="todelc"),
    path('todel1/<todo_id>', views.deleteone, name="todel1"),
    path('entry/', views.index, name="index"),
    path('entry/<int:pk>',views.details, name= "details"),
    path('entry/add',views.add,name='add'),
    path('entry/delete/<int:pk>',views.delete,name='delete'),
    path('entry/edit/<int:pk>',views.update,name='update'),
    path('admin/', admin.site.urls),
]
