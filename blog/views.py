from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):

    context =  {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html',context)

def about(request):

    return render(request, 'blog/about.html')

def register(request):

    return HttpResponse('<h1>Blog Register</h1>')

def profile(request):

    return HttpResponse('<h1>Blog Profile</h1>')
