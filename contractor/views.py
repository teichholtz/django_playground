from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Contractor Home</h1>')

def about(request):
    return HttpResponse('<h1>Contractor about</h1>')

def register(request):
    return HttpResponse('<h1>contractor register</h1>')

def profile(request):
    return HttpResponse('<small>Contractor profile</small>')
