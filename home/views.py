from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('hello this is home')
    return render(request,"home.html")


def projects(request):
    # return HttpResponse('hello this is services')
    return render(request,"projects.html")


def about(request):
    # return HttpResponse('hello this is about')
    return render(request,"about.html")


def contact(request):
    # return HttpResponse('hello this is contact')
    return render(request,"contact.html")
