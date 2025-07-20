from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.messages import success,error
from django.contrib.auth.models import User

# Create your views here.

def manage(request):
    if not request.user.is_authenticated:
        error(request,f"Login first !!!")
        return redirect('login')
    StuData = Students.objects.all()
    
    context = {
        "StuData":StuData,
    }
    return render(request,'manage.html',context)



def form(request):
    if not request.user.is_authenticated:
        error(request,f"Login first !!!")
        return redirect('login')
    if request.method == 'POST':

        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        profilePic = request.FILES.get('profilePic')
        resume = request.FILES.get('resume')


        Students.objects.create(name=name,age=age,email=email,profilePic=profilePic,resume=resume)
        return redirect('manage')
    
    return render(request,'form.html')


from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.messages import success,error

    


def update(request,id):
    if not request.user.is_authenticated:
        error(request,f"Login first !!!")
        return redirect('login')
    StuData = Students.objects.filter(id=id).first()
    if request.method == 'POST':

        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        profilePic = request.POST.get('profilePic')
        resume = request.POST.get('resume')



        StuData.name = name
        StuData.age = age
        StuData.email = email
        profilePic = profilePic
        resume = resume

        StuData.save()

        return redirect('manage')
    
    return render(request,'update.html')
    

def delete(request,id):
    if not request.user.is_authenticated:
        error(request,f"Login first !!!")
        return redirect('login')
    StuData = Students.objects.filter(id=id).first()

    StuData.delete()
    

    return redirect('manage')


def activate(request,id):
    if not request.user.is_authenticated:
        error(request,f"Login first !!!")
        return redirect('login')
    StuData = Students.objects.filter(id=id).first()

    if StuData:
        StuData.is_active = True
        StuData.save()
    
    return redirect('manage')



def deactivate(request, id):
    if not request.user.is_authenticated:
        error(request,f"Login first !!!")
        return redirect('login')
    StuData = Students.objects.filter(id=id).first()

    if StuData:
        StuData.is_active = False
        StuData.save()

    return redirect('manage')


from django.shortcuts import render, redirect 
from .models import Students



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("\n username =", username)
        print("\n password =", password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome {user.username}")
            print("login successfull")
            return redirect('manage')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')



def logout(request):
    if not request.user.is_authenticated:
        error(request,f"Login first !!!")
        return redirect('login')
    auth_logout(request)
    success(request, f"Good by! {request.user.usename}")
  
    return redirect('login')
        


def register(request):
    # if not request.user.is_authenticated:
    #     error(request,f"Login first !!!")
    #     return redirect('login')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')

        print("username =",username)
        print("password =",password)
        print("confirmpassword =",confirmpassword)

        if password == confirmpassword:
            
            User.objects.create_user(username=username,password=password)
            return redirect('login')
        else:
            return render(request,'register.html')


    return render(request,'register.html')




#static method --

def nav(request):

    return render(request,'base.html')

def inherit(request):

    return render(request,'inherit.html')




