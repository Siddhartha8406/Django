from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse

def index(request):
    template = loader.get_template('authentication/index.html')
    return render(request, 'authentication/index.html')

def login(request):
    if request.method == 'POST':
        x=request.POST['username']
        y=request.POST['password']
        user = authenticate(request, username=x, password=y)
        print(user)
        if user==None:
            messages.error(request=request, message='Bad Credentials')
            return redirect(login)
        else:
            messages.success(request=request, message='Login successful')
            return redirect(login)
    else:
        return render(request, 'authentication/login.html')

def signup(request):
    if request.method == 'POST':
        userName = request.POST['username']
        pwd= request.POST['password']
        confirm = request.POST['confirmPassword']

        
        user = User.objects.create_user(username= userName, password=pwd)
        user.save()
        # messages.add_message(request, messages.SUCCESS, "Welcome " + userName)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'authentication/signup.html')

def logout(request):
    pass

def delete(request):
    if request.method == 'POST':
        userName = request.POST['username']
        print(userName)
        user = User.objects.get(username=userName)
        user.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'authentication/delete_user.html')