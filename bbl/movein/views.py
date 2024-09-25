from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'movein/index.html')

def t_login(request):
    return render(request, 'movein/t_login.html')

def l_room(request):
    return render(request, 'movein/l_roompage.html')

def t_myRoom(request):
    return render(request, 'movein/t_myRoom.html')
