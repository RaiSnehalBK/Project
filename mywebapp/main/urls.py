from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('location/', views.location, name='location'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),    
    path('logout/', views.logout, name='logout'),    
    path("video_feed/", views.video_feed, name="video_feed"),
    path("profile/update/", views.update_profile, name="update_profile"),
    path("profile/upload-photo/", views.upload_photo, name="upload_photo"),
    
]