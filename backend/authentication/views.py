from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User
import json

# from .models import profile




def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        temp = request.POST.get('email')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request,user)
            return redirect('Homepage')
        else:
            return render(request, 'signup.html',{'form':form})
    else:
        form = UserRegisterForm()
        return render(request, 'signup.html',{'form':form})


def signin(request):
    if request.user.is_authenticated:
        return render(request,'homepage.html')
    if request.method =='POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username = username, password = password1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request,'signin.html',{'form':form})
    else:
        form = AuthenticationForm()
        return render(request,'signin.html',{'form':form})

def signin_ajax(request):
    if request.method == "POST":
        data=json.loads(request.body.decode('UTF-8'))
        print(data["username"]," ",data["password"])

        
def signout(request):
    logout(request)
    return redirect('/')






