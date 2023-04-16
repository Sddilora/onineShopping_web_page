from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="home"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("callback/", views.callback, name="callback"),
    path("mypage/", include('testpages.urls'), name = "testpages"),
]