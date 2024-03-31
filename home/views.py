from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import date

def index(request):
    context = {}
    return render(request, "home/index.html", context)


def contact(request):  
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        reason = request.POST.get('reason')
        mssg = request.POST.get('mssg') 
        cont = Contact.objects.create(name=name, email=email, reason=reason, mssg=mssg)  
        messages.success(request, "Thank you for contacting us!")
        return redirect("/")  
    context = {'today': date.today()}
    return render(request, 'home/contact.html', context)

def zoom(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')  
        date = request.POST.get('date')
        time = request.POST.get('time')
        zom = Zoom.objects.create(name=name,email=email,date=date,time=time)
        messages.success(request, "We will send you an email before 24 hours of the zoom call.")
        return redirect("/")  
    context = {}
    return render(request,'home/zoom.html',context)

def about(request):
    context = {}
    return render(request,'home/about.html',context)