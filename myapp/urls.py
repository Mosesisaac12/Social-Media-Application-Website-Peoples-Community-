from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('setting/', views.setting, name='setting'),
    path('member-profile/<str:pk>/', views.member_profile, name='member-profile'),
    path('member-media-all/<str:pk>', views.member_media_all, name='member-profile'),
    path('member-activity-personal', views.member_activity_personal, name='member-activity-personal'),
    path('signup', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('member_friends', views.member_friends, name='member-friends'),
]
