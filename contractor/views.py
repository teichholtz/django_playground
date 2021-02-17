from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'contractor/home.html')

def about(request):
    return render(request, 'contractor/about.html')

def register(request):
    return HttpResponse('<h1>contractor register</h1>')

def profile(request):
    return HttpResponse('<small>Contractor profile</small>')
