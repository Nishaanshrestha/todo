from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .login_form import LoginForm
from .signup_form import SignupForm

def signup(request):
    return render(request,'signup.html')
def login_view(request):
    # if request.method == 'POST':
        # username=request.POST['username']
        # password=request.POST['password']
        
        # user=authenticate(request,username=username,password=password)
        # if user:
        #     login(request,user)
        #     return redirect('home')
        # else:
    # context={'error':'individuals user credentials'}
    # return render(request,'home.html',context)
    # return render(request,'login.html')

    login_form=LoginForm(request.POST)
    if login_form.is_valid():
        # print(login_form.cleaned_data)
        username=login_form.cleaned_data['username']
        password=login_form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:

            login_form.add_error(None,'Username or Password is incorrect')
            contex={'login_form':login_form}
            return render(request,'login.html',contex)
        
        # user=authenticate(request,username=username,password=password)
        # if user:
        #     login(request,user)
        #     return redirect('home')
        # else:
    # context={'error':'individuals user credentials'}
    # return render(request,'home.html',context)
    # return render(request,'login.html')

    login_form=LoginForm()
    contex={'login_form':login_form}
    return render(request,'login.html',contex)

def profile(request):
    return render(request,'profile.html') 

def home(request):
    return render(request,'home.html')
def logout(request):
    pass

def signup(request):
    # username = request.POST['username']
    # email = request.POST['email']
    # password = request.POST['password']
    # user = User.objects.create_user(username = username, email = email, password = password)

    # if user:
    #     context = {'success': 'succesfully user created!!'}
    #     return render(request, 'login.html', context)
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            # user=User(
            #     # username=form.cleaned_data['username'],
            #     # email=form.cleaned_data['email'],
            #     # password=form.cleaned_data['password1']
               
            # )
            
                user=form.save()
                user.refresh_form_db()
                user.save()
                return redirect('login')
    else:
        signup_form=SignupForm()
    return render(request,'signup.html',{'form':signup_form})
