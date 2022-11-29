from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import userCred

def index(request):
    template = loader.get_template('authentication/index.html')
    return render(request, 'authentication/index.html')

def login(request):
    return render(request, 'authentication/login.html')

def create(request):
    userName = request.POST['username']
    pwd= request.POST['password']
    confirm = request.POST['confirmPassword']

    
    user = userCred(username=userName, password = pwd)
    user.save()
    # messages.add_message(request, messages.SUCCESS, "Welcome " + userName)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
    return render(request, 'authentication/signup.html')

def logout(request):
    pass