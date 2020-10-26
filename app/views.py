from django.shortcuts import render,redirect, get_object_or_404
from .models import Video, Comment_Model, ReplyModel, Rating
from .forms import VideoUpload, CommentForm, ReplyCommentForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.


@login_required(login_url='login')
def file_upload(request):
    form = VideoUpload()
    user_id = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = VideoUpload(request.POST or None, request.FILES or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = user_id
            form_obj.save()
            return redirect('profile')
    return render(request, 'app/upload.html', {'form': form})


def show_video(request): # Show Video List in UI
    videos= Video.objects.filter(make_privet=False).order_by('-created_on')
    if videos is not None:
        return render(request, 'app/index.html', {'video': videos})


@login_required(login_url='login')
def add_ratting(request, video_id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        try:
            ratings = Rating.objects.get(video_id=video_id, user=request.user)
            ratings.delete()
        except:
            ratings = None
        rating = request.POST.get('rating')
        rating_obj = Rating(user=request.user, video_id=video_id, rating=rating)
        rating_obj.save()
        return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


def play_video(request, id): # Show clicked Video with list into UI
    url = request.META.get('HTTP_REFERER')
    video = Video.objects.get(pk=id)
    list = Video.objects.all().order_by('-created_on')
    comments = Comment_Model.objects.filter(is_aproved=True, comment_video=video)
    ratings = Rating.objects.filter(video=video)

    if request.method =='POST':
        url = request.META.get('HTTP_REFERER')
        user_id = User.objects.get(id=request.user.id)
        comment_form = CommentForm(request.POST)

        # comment section
        if comment_form.is_valid():
            comment_obj = comment_form.save(commit=False)
            comment_obj.comment_video = video
            comment_obj.comment_user=user_id
            comment_obj.save()
            return HttpResponseRedirect(url)


    total_rating =0
    avg_rating = 0
    no_rating = len(ratings)
    if ratings is not None:
        for rating in ratings:
            total_rating += rating.rating
            avg_rating = total_rating / no_rating;
            avg_rating= round(avg_rating, 1)


    rating_form = RatingForm()
    comment_form = CommentForm()
    context={'video': video,
             'list': list,
             'comments': comments,
             'comment_form': comment_form,
             'rating_form':rating_form,
             'no_rating':no_rating,
             'avg_rating': avg_rating, }
    return render(request, 'app/play.html', context)


@login_required(login_url='login')
def comment_reply(request, id):
    url = request.META.get('HTTP_REFERER')
    parent_comment = Comment_Model.objects.get(pk=id)
    child_comment = ReplyModel.objects.filter(comment=id)
    comment_form = ReplyCommentForm()
    if request.method == 'POST':
        comment_form = ReplyCommentForm(request.POST)
        if comment_form.is_valid():
            reply_obj = comment_form.save(commit=False)
            reply_obj.comment = parent_comment
            reply_obj.comment_user = request.user
            reply_obj.save()
            return HttpResponseRedirect(url)

    context= {
        'comment': parent_comment,
        'replys': child_comment,
        'form': comment_form

    }
    return render(request, 'app/reply.html', context)


@login_required(login_url='login')
def delete_view(request, id):
    url = request.META.get('HTTP_REFERER')
    video = Video.objects.get(pk=id)
    video.delete()
    return HttpResponseRedirect(url)


@login_required(login_url='login')
def delete_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    comment = Comment_Model.objects.get(pk=id)
    comment.delete()
    return HttpResponseRedirect(url)


@login_required(login_url='login')
def delete_reply(request, comment, reply):
    url = request.META.get('HTTP_REFERER')
    reply_comment = ReplyModel.objects.get(pk=reply)
    reply_comment.delete()
    return HttpResponseRedirect(url)

