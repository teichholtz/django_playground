from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# the 'username' is in the django form.  It can be
# renamed.

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            emailaddress=form.cleaned_data.get('email')
            messages.success(request,f'Account has been created for {username} with {emailaddress}')
            return redirect('blog-home')
    else:
        form=UserRegisterForm()

    return render(request,'users/register.html', {'form':form})
