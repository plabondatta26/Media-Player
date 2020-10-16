from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('login/', views.Loginview, name='login'),
    path('logout/', views.LogoutView, name= 'logout'),
    path('register/', views.RegisterView, name='register'),
    path('profile/', views.Profile, name='profile'),
    path('profile/update/', views.UpdateProfile, name='update_profile'),
    path('profile/change_pp/', views.Profile_pic_upload, name='change_p_pic'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
