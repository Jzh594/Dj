# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    string = u"使用Django来建网站"
    TutorialList = ["HTML","CSS","jQuery","Python","Django"]
    info_dict = {'site': u'Django','content': u'IT技术'}
    List = map(str,range(100))
    #return render(request, 'home.html', {'string': string})
    #return render(request,'home.html',{'TutorialList':TutorialList})
    #return render(request,'home.html',{'info_dict':info_dict})
    return render(request,'home.html',{'List':List})
    
    
def add(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
    
def grade(request,var):
    var = int(var)
    return render(request,'home.html',{'var':var})