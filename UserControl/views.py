from django.shortcuts import render,redirect, get_object_or_404
from .forms import RegisterForm, Update_Profile, Update_Profile_Pic#, Captcha
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import Video
from .models import CreateProfile
from django.contrib import messages


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

"""
@login_required(login_url='login')
def ResetPasswordView(request):
    fm = Captcha()
    return render(request, 'UserControl/resetps.html',{'fm':fm})
"""



@login_required(login_url='login')
def Profile(request):
    usr= request.user
    details =get_object_or_404(CreateProfile, user=usr)
    post = Video.objects.filter(user=usr)
    return render(request, 'UserControl/profile.html',{'post':post, 'details':details})


@login_required(login_url='login')
def UpdateProfile(request):

    profile = CreateProfile.objects.get(user=request.user)
    form= Update_Profile(instance=profile)
    if request.method=='POST':
        form= Update_Profile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'UserControl/UpdateProfile.html', {'profile': profile})
    context={
        'form':form
    }
    return render(request, 'UserControl/UpdateProfile.html', context)

@login_required(login_url='login')
def Profile_pic_upload(request):
    profile = CreateProfile.objects.get(user=request.user)
    form = Update_Profile_Pic(instance=profile)
    if request.method == 'POST':
        form = Update_Profile_Pic(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'UserControl/profile_pic.html', {'form': form})


