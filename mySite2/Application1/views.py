from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import application1

def index(request):
    return HttpResponse("Hello World")

def testIndex(request):
    return HttpResponse("Byee World")

def template1(req):
    template1 = loader.get_template("mySite1.html")
    return HttpResponse(template1.render())

def viewTables(requests):
    tableData = application1.objects.all().values()
    template1 = loader.get_template("index.html")
    context = {
        "mymembers": tableData,
    }
    return HttpResponse(template1.render(context, requests))

def add(requests):
    template1 = loader.get_template("add.html")
    return HttpResponse(template1.render({}, requests))

def addrecord(requests):
    x=requests.POST['first']
    y=requests.POST['last']
    member = application1(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(requests, id):
    member = application1.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(requests, id):
    member = application1.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        'myMember': member
    }
    return HttpResponse(template.render(context, requests))

def updateRecord(requests, id):
    first = requests.POST['first']
    last = requests.POST['last']
    member = application1.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))