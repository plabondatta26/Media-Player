from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Loginview(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('home')

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