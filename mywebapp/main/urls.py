from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),    
    path('logout/', views.logout, name='logout'),    
    path("video_feed/", views.video_feed, name="video_feed"),
    
]
