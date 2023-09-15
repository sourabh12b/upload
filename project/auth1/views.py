from django.shortcuts import render
from .forms import signupform,LogInFrom
from django.contrib import messages
from django.contrib.auth  import authenticate,login,logout


def signup(req):
    if req.method=="POST":
        fm=signupform(req.POST) #explicility mention
        if fm.is_valid():
            fm.save()
            messages.success(req,'signup successful')
            return render(req,'auth1/signup.html',{'fm':fm})
    else:
        fm=signupform()
    return render(req,'auth1/signup.html',{'fm':fm})


def log_in(req):
    global Username
    if req.method=="POST":
        fm=LogInFrom(request=req,data=req.POST)
        if fm.is_valid():
            Username=fm.cleaned_data["username"]
            b=fm.cleaned_data["password"]
        user=authenticate(username=Username,password=b)
        if user is not None:
            messages.success(req,"LOGIN SUCCESSFUL")
            fm=LogInFrom()
            return render(req,"auth1/login.html",{'fm':fm})
    else:
        fm=LogInFrom()
    return render(req,'auth1/login.html',{'fm':fm})

def log_out(req):
    logout(req)
    messages.success(req,"logout sucessfully")
    fm=signupform()
    return render(req,"auth1/signup.html",{'fm':fm})

# Create your views here.
