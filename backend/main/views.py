from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *

def index(request):
    if request.method == 'POST':
        ttl = request.POST.get('title')
        decx = request.POST.get('decs')
        a = todo()
        a.user = request.user
        a.title = ttl
        a.dec = decx
        a.save()
    try:
        data = todo.objects.filter(user = request.user)
    except:
        data = None
    return render(request,'index.html',{'data':data})

def sinsr(request):
    if request.method == 'POST':
        dec = request.POST.get('decs')
        a = sins()
        a.desc = dec
        a.user = request.user
        a.save()
        return redirect('diary')
    return render(request,'sins.html')

def goodsr(request):
    if request.method == 'POST':
        dec = request.POST.get('decs')
        a = goods()
        a.desc = dec
        a.user = request.user
        a.save()
        return redirect('diary')
    return render(request,'goods.html')

def diary(request):
    sin = sins.objects.filter(user = request.user)
    conf = goods.objects.filter(user = request.user)
    content = {
        'sins' : sin,
        'conf': conf
    }
    return render(request,'diary.html',context=content)