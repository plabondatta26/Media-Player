from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from UserControl import views as us
from . import views

urlpatterns = [
    path('', views.showvideo, name='home'),
    path('upload/',views.File_upload, name='upload'),
    path('play/<int:id>/', views.play_video, name='play'),
    path('reply/<int:vedioId>/<int:id>/', views.CommentReply, name='reply'),
    path('delete/<int:id>/', views.DeleteView, name= 'delete'),
    path('add_rating/<int:video_id>/', views.add_ratting, name='add_rating'),
    path('delete_comment/<int:id>/', views.DeleteComment, name='delete_comment'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
