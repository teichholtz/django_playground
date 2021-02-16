from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'davet',
        'title': 'blog post 1',
        'content': 'First post',
        'date_posted': 'Feb 15, 2020',
    },
    {
        'author': 'Mary',
        'title': 'blog post 2',
        'content': 'second post',
        'date_posted': 'Feb 16, 2020',
    }
]

def home(request):

    context =  {
        'posts': posts
    }

    return render(request, 'blog/home.html',context)

def about(request):

    return render(request, 'blog/about.html')

def register(request):

    return HttpResponse('<h1>Blog Register</h1>')

def profile(request):

    return HttpResponse('<h1>Blog Profile</h1>')
