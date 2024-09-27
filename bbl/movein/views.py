from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .form import *

# Create your views here.
def t_myRoom(request):
    return render(request, 'movein/t_myRoom.html')

def index(request):
    return render(request, 'movein/index.html')

def t_login(request):
    return render(request, 'movein/t_login.html')

def l_room(request):
    return render(request, 'movein/l_roompage.html')

def l_announcement(request):
    announcements = Announcements.objects.all()
    return render(request, 'movein/l_announcement.html', {'announcements': announcements})

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