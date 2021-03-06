from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views as app
from UserControl import views as user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', user.about_developer, name='about'),

    path('', app.show_video, name='home'),
    path('upload/', app.file_upload, name='upload'),
    path('play/<int:id>/', app.play_video, name='play'),
    path('reply/<int:id>/', app.comment_reply, name='reply'),
    path('delete/<int:id>/', app.delete_view, name='delete'),
    path('add_rating/<int:video_id>/', app.add_ratting, name='add_rating'),
    path('delete_comment/<int:id>/', app.delete_comment, name='delete_comment'),
    path('delete_reply/<int:comment>/<reply>/', app.delete_reply, name='delete_reply'),


    path('login/', user.login_view, name='login'),
    path('logout/', user.logout_view, name='logout'),
    path('register/', user.register_view, name='register'),
    path('profile/', user.profile, name='profile'),
    path('profile/update/', user.update_profile, name='update_profile'),
    path('profile/change_pp/', user.profile_pic_upload, name='change_p_pic'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
