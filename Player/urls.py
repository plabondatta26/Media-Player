from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from app.views import File_upload, showvideo,play_video, DeleteView, EditView
from UserControl import views as us

urlpatterns = [
    path('admin/', admin.site.urls),
    url('upload/', File_upload, name='upload'),
    path('', showvideo, name='home'),
    path('play/<int:id>/', play_video, name='play'),
    path('delete/<int:id>/', DeleteView, name= 'delete'),
    path('edit/<int:id>/', EditView, name= 'edit'),

    path('login/', us.Loginview, name='login'),
    path('logout/', us.LogoutView, name= 'logout'),
    path('register/', us.RegisterView, name='register'),
    path('reset/', us.ResetPasswordView, name='reset'),
    path('profile/', us.Profile, name='profile'),



]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

