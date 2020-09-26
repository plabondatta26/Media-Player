from django.shortcuts import render,redirect
from .forms import RegisterForm, Captcha
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import Video

# Create your views here.
def Loginview(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile')

        return render(request, 'UserControl/login.html')

def RegisterView(request):
    if request.method=='POST':
        fm= RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
        else:
            redirect('register')
    fm= RegisterForm()
    return render(request, 'UserControl/register.html',{'fm':fm})

@login_required(login_url='login')
def LogoutView(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def ResetPasswordView(request):
    fm = Captcha()
    return render(request, 'UserControl/resetps.html',{'fm':fm})


@login_required(login_url='login')
def Profile(request):
    usr= request.user.id
    usrp = User.objects.filter(pk=usr)
    post = video= Video.objects.filter(user=usr)
    return render(request, 'UserControl/profile.html',{'post':post})
