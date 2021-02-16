from django.urls import path
from . import views


# make the path arg '' since right now
# it is the home page.  And the view it will
# direct to is views.home.



urlpatterns = [
    path('', views.home, name='contractor'),
    path('about', views.about, name='contractor-about'),
    path('register',views.register,name='blog-register'),
    path('profile',views.profile,name='blog-profile')
]
