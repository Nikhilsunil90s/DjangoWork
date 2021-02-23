from django.shortcuts import render , redirect
from .forms import RegisterForm
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login 

# Create your views here.
def Login(request):
    print("LOGIN REQUEST")
    if request.method == 'POST':
        print("POST REQUEST")
        uname = request.POST['username']            
        pwd = request.POST['password']
        user = authenticate(request , username = uname, password= pwd)
        print(uname, pwd)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            messages.info(request,f"Hello, {uname}! , Invalid Credentials\n Please check or Register Again!")
            return redirect('Login')
    else:
        af = AuthenticationForm()    
        return render(request , 'user/login.html' , {'AuthenticationForm' : af})

def register(request):
    if request.method == 'POST':
        rf = RegisterForm(request.POST)
        if rf.is_valid():
            rf.save()
            uname = rf.cleaned_data['username']
            em =rf.cleaned_data.get('email')
            pn = rf.cleaned_data.get('phone_no')
            print(uname, em, pn)
            messages.success(request, f"Hello, {uname}!\nYour Account Has Been Created!\nPlease Login Now...")
            return redirect('register-success')
    else:
        rf = RegisterForm()
        return render(request , 'user/register.html' , {'RegisterForm' : rf})


def register_success(request):
    return render(request, 'user/register-success.html')