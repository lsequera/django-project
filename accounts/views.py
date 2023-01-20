from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.http import HttpResponse

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
            user.save()
            return HttpResponse('User created successfully!')
        else:
            return HttpResponse('Passwords do not coincide, check the fields and try again!')

def signin(request):
    return HttpResponse('Login')

def logout(request):
    return HttpResponse('Logout')