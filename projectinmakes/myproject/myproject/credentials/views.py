from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
def register(request):
    if request.method=='POST':
        user_name=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username is already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect('login')
                print('user created')
        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'username or password must be incorrect')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
