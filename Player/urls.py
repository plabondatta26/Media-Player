"""Player URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from app.views import File_upload, showvideo,play_video
from UserControl import views as us

urlpatterns = [
    path('admin/', admin.site.urls),
    url('upload/', File_upload, name='upload'),
    path('', showvideo, name='home'),
    path('play/<int:id>/', play_video, name='play'),
    path('login/', us.Loginview, name='login'),
    path('register/', us.RegisterView, name='register'),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

