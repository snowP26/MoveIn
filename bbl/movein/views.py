from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .form import *

def index(request):
    return render(request, 'movein/index.html')

# Owner Views
def l_room(request):
    context = {
        'active_link': 'rooms',
    }
    return render(request, 'movein/l_roompage.html')

def l_announcement(request):
    announcements = Announcements.objects.all()
    context = {
        'announcements': announcements,
        'active_link': 'announcements',
    }
    return render(request, 'movein/l_announcement.html', context)

def announcement_view(request):
    if request.method == "POST":
        form = announcementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landlord_announcement') 
    else: 
        form = announcementForm()

    return render(request, 'movein/announcement_create.html', {'form': form} ) 

def announcement_create(request):
    return render(request, 'movein/announcement_create.html')


# Tenant Views
def t_myRoom(request):
    context = {
        'active_link': 'rooms',
    }

    return render(request, 'movein/t_myRoom.html', context)

