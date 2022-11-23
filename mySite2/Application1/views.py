from django.http import HttpResponse
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

def addRecord(requests):
    template1 = loader.get_template("add.html")
    return HttpResponse(template1.render({}, requests))
    