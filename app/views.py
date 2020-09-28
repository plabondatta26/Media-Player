from django.shortcuts import render,redirect
from .models import Video, Comment_Model
from .forms import video_upload, commentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def File_upload(request):
    form= video_upload()
    if request.user.is_authenticated:
        user_id = User.objects.get(id=request.user.id)
        if request.method=='POST':
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
    user_id = User.objects.get(id=request.user.id)
    video = Video.objects.get(pk=id)
    list = Video.objects.all()
    comments = Comment_Model.objects.filter(comment_video=id)
    comment_form = commentForm()
    if request.method=='POST':
        if request.user.is_authenticated:
            comment_form = commentForm(request.POST)
            if comment_form is not None:
                if comment_form.is_valid():
                    fm_obj = comment_form.save(commit=False)
                    fm_obj.comment_user = User.objects.get(pk=request.user.id)
                    fm_obj.comment_video = video
                    fm_obj.save()
                    return render(request, 'app/play.html', {'video':video, 'list':list, 'comments':comments,'comment_form':comment_form})
    return render(request, 'app/play.html', {'video':video, 'list':list, 'comments':comments,'comment_form':comment_form})




@login_required()
def DeleteView(request, id):
    video= Video.objects.get(pk=id)
    video.delete()
    return redirect('profile')


"""
@login_required()
def EditView(request, id):
    usr = request.user
    video= Video.objects.get(pk=id)
    fm = video_upload(request.POST or None, request.FILES or None, instance=usr)
    if fm.is_valid():
        fm.save(commit=True)
        return redirect('profile')
    fm= video_upload()
    return render(request, 'app/Edit.html', {'fm':fm, 'video':video})
"""