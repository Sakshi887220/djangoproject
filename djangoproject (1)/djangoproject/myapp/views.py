from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import datetime

from django.template import loader  

def index(request):  
    template = loader.get_template('index.html') # getting our template  
    name = {  
        'student':'rahul'  
    }  
    return HttpResponse(template.render(name))       
   
 
# create a function
def currentdate(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


