from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User 
from django.contrib.auth import login,authenticate
from django.contrib import messages
import time

# Create your views here.
def register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        messages.success(request,"Qeydiyyat ugurla tamamlandi")
        time.sleep(3)
        #login(request, newUser)
        return redirect("home")
    context={
            "form":form
        }
    return render(request,"register.html",context)    
   


    """if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            newUser=User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            return redirect("home")
        context={
            "form":form
        }
        return render(request,"register.html",context)
    else:
        form = RegisterForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)

    # form = RegisterForm()
    # context={
    #     "form":form
    # }
    # return render(request,"register.html",context)"""


def login(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Username ve ya Password yalnisdir")
            return render(request,"login",context)
        else:
            messages.success(request,"Giris ugurla tamamlandi))")
            login(request,user)
            return redirect(request,"home")
        
    return render(request,"login.html",context)
def logout(request):
    return render(request,"logout.html")