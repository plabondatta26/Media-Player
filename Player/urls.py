from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from app import views as media_player_views
from UserControl import views as us


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    path('', media_player_views.showvideo, name='home'),
    url('upload/',media_player_views.File_upload, name='upload'),
    path('play/<int:id>/', media_player_views.play_video, name='play'),
    path('delete/<int:id>/', media_player_views.DeleteView, name= 'delete'),
    #path('edit/<int:id>/', EditView, name= 'edit'),
    path('delete_comment/<int:id>/', media_player_views.DeleteComment, name='delete_comment'),

    path('login/', us.Loginview, name='login'),
    path('logout/', us.LogoutView, name= 'logout'),
    path('register/', us.RegisterView, name='register'),
    #path('reset/', us.ResetPasswordView, name='reset'),
    path('profile/', us.Profile, name='profile'),
    path('profile/update/', us.UpdateProfile, name='update_profile'),
    path('profile/change_pp/', us.Profile_pic_upload, name='change_p_pic'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
