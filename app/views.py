from django.shortcuts import render,redirect, get_object_or_404
from .models import Video, Comment_Model, ReplyModel
from .forms import video_upload, commentForm, ReplyCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

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
    url = request.META.get('HTTP_REFERER')
    user_id = User.objects.get(id=request.user.id)
    video = Video.objects.get(pk=id)
    list = Video.objects.all()
    comments = Comment_Model.objects.filter(is_aproved=True)
    if request.method =='POST':
        comment_form= commentForm(request.POST)
        if comment_form.is_valid():
            comment_obj = comment_form.save(commit=False)
            comment_obj.comment_video = video
            comment_obj.comment_user=user_id
            comment_obj.save()
            return HttpResponseRedirect(url)
    comment_form = commentForm()
    context={'video': video,
             'list': list,
             'comments': comments,
             'comment_form': comment_form}
    return render(request, 'app/play.html', context)

def CommentReply(request,vedioId, id):
    url = request.META.get('HTTP_REFERER')
    video = Video.objects.get(pk=vedioId)
    parent_comment= Comment_Model.objects.get(pk=id)
    print(parent_comment.created)
    child_comment = ReplyModel.objects.filter(comment_video=vedioId, comment=id)
    comment_form = ReplyCommentForm()
    if request.method=='POST':
        comment_form= ReplyCommentForm(request.POST)
        if comment_form.is_valid():
            reply_obj= comment_form.save(commit=False)
            reply_obj.comment_video= video
            reply_obj.comment=parent_comment
            reply_obj.comment_user=request.user
            reply_obj.save()
            return HttpResponseRedirect(url)

    context= {
        'comment':parent_comment,
        'replys':child_comment,
        'form':comment_form

    }
    return render(request,'app/reply.html', context)

@login_required()
def DeleteView(request, id):
    video= Video.objects.get(pk=id)
    video.delete()
    return redirect('profile')

@login_required(login_url='login')
def DeleteComment(request,id):
    if request.user.is_authenticated:
        comment = Comment_Model.objects.get(id=id)
        video= str(comment.comment_video.id)
        comment.delete()
        link = '/play/'+video+'/'
        return redirect(link)

"""
@login_required(login_url='login')
def EditComment(request,id):
    comment = Comment_Model.objects.get(id=id)
    video = str(comment.comment_video.id)
    commentForm(request.POST)
    
    link = '/play/' + video + '/'
    return redirect(link) """

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
