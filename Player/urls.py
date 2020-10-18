from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views as app
from UserControl import views as user
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', app.showvideo, name='home'),
    path('upload/',app.File_upload, name='upload'),
    path('play/<int:id>/', app.play_video, name='play'),
    path('reply/<int:id>/', app.CommentReply, name='reply'),
    path('delete/<int:id>/', app.DeleteView, name='delete'),
    path('add_rating/<int:video_id>/', app.add_ratting, name='add_rating'),
    path('delete_comment/<int:id>/', app.DeleteComment, name='delete_comment'),
    path('delete_reply/<int:comment>/<reply>/', app.DeleteReply, name='delete_reply'),


    path('login/', user.Loginview, name='login'),
    path('logout/', user.LogoutView, name='logout'),
    path('register/', user.RegisterView, name='register'),
    path('profile/', user.Profile, name='profile'),
    path('profile/update/', user.UpdateProfile, name='update_profile'),
    path('profile/change_pp/', user.Profile_pic_upload, name='change_p_pic'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
