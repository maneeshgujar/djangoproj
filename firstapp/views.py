from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader 

from .models import Member, person

# Create your views here.
def func(request):
    # return HttpResponse("Hello world!")

    template= loader.get_template('myfirst.html')
    return HttpResponse(template.render())

   

def memfunc(request):
    #mongo database
    mem= person.find({}) 
    # print(mem)
    # mem = Member.objects.all().values()
    # mem = person.objects.all().values()
    # mem = Member.objects.all().order_by('phno')
    # mem = Member.objects.filter(lastname__startswith="g").values()
    template= loader.get_template('allmembers.html')
    context={
        'mymembers':mem,
    }
    # for x in context:
    #     print(x)
    return HttpResponse(template.render(context,request))
    # return HttpResponse("hello")

def detailsfunc(request,id):
    mem= person.find_one({'phno':id})

    # mem = Member.objects.get(id=id)
    template= loader.get_template('details.html')
    context={
        'x':mem,
    }
    return HttpResponse(template.render(context,request))

def mainfunc(request):

    
    template= loader.get_template('main.html')
    return HttpResponse(template.render())