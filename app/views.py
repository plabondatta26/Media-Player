from django.shortcuts import render,redirect
from .models import Video
from .forms import video_upload

# Create your views here.
def File_upload(request): # Upload a Video
    form = video_upload(request.POST or None, request.FILES or None)
    if form is not None:
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/upload.html', {'form': form})

def showvideo(request): # Show Video List in UI
    video= Video.objects.all()
    if video is not None:
        return render(request, 'app/index.html', {'video': video})

def play_video(request, id): # Show clicked Video with list into UI
    print('id=',id)
    video = Video.objects.get(pk=id)
    list = Video.objects.all()

    return render(request, 'app/play.html', {'video':video, 'list':list})