from django.shortcuts import render,redirect
from .models import Video
from .forms import video_upload
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def File_upload(request):
    form= video_upload()
    if request.user.is_authenticated:
        user_id = User.objects.get(id=request.user.id)
        print(user_id)
        if request.method=='POST':
            print('post')
            form= video_upload(request.POST or None, request.FILES or None)
            if form.is_valid():
                form_obj = form.save(commit=False)
                form_obj.user= user_id
                form_obj.save()
                return redirect('profile')
        form = video_upload()
        return render(request, 'app/upload.html', {'form': form})


def showvideo(request): # Show Video List in UI
    video= Video.objects.filter(make_privet=False).order_by('-created_on')
    if video is not None:
        return render(request, 'app/index.html', {'video': video})

def play_video(request, id): # Show clicked Video with list into UI
    video = Video.objects.get(pk=id)
    list = Video.objects.all()
    return render(request, 'app/play.html', {'video':video, 'list':list})


@login_required()
def DeleteView(request, id):
    print('id=',id)
    video= Video.objects.get(pk=id)
    video.delete()
    return redirect('profile')


@login_required()
def EditView(request, id):
    usr = request.user
    video= Video.objects.get(pk=id)
    print(video)
    fm = video_upload(request.POST or None, request.FILES or None, instance=usr)
    if fm.is_valid():
        print('valid')
        fm.save(commit=True)
        return redirect('profile')
    fm= video_upload()
    return render(request, 'app/Edit.html', {'fm':fm, 'video':video})