from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

def signup(request):
    return render(request,'signup.html')
def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            context={'error':'individuals user credentials'}
            return render(request,'home.html',context)
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html') 

def home(request):
    return render(request,'home.html')
def logout(request):
    pass
