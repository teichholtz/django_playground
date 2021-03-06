from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('register', views.register, name='blog-register'),
    path('frap/', views.about, name='frap-about'),
    path('profile', views.profile, name='blog-profile')
]

