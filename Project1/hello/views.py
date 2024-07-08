from django.shortcuts import render,redirect,HttpResponse
from hello.models import Signup
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def SignupPage(request):
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        Username = request.POST.get('Username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address = request.POST.get('address')
        Spage = Signup(firstName=firstName,lastName=lastName,Username=Username,email=email,password=password,address=address,date=datetime.today())
        Spage.save()
        myuser = User.objects.create_user(Username,email,password)
        myuser.firstname = firstName
        myuser.lastname = lastName
        myuser.save()
        messages.success(request, "Your acc has created succesfully")
    return render(request,'SignupPage.html')

def LoginPage(request):
    if request.method == "POST":
        UserName = request.POST["UserName"]
        Password = request.POST["Password"]
        
        # check user entered info 
        user = authenticate(request,username=UserName, password=Password)
        print(UserName,Password) 
        if user is not None:
            login(request,user)
            messages.success(request,"sucessfully Logged in")
            return redirect("index")
        else:
            messages.error(request,"Invalid Credentials,please try again")
            return render(request,'LoginPage.html')
    return render(request,'LoginPage.html')

def Logout(request):
    logout(request)
    messages.success(request,"sucessfully Logged out")
    return redirect("LoginPage")

