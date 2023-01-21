from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from django.http import HttpResponse

from .forms import CreateUser

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form' : CreateUser
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
            user.save()
            return render(request, 'login.html', {
                "form": AuthenticationForm,
                "msg" : "User created successfully!"
                })
        else:
            return HttpResponse('Passwords do not coincide, check the fields and try again!')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            "form": AuthenticationForm
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                "form": AuthenticationForm, 
                "error": "Username or password is incorrect."
                })

        login(request, user)
        return redirect('index')

@login_required
def signout(request):
    logout(request)
    return redirect('index')