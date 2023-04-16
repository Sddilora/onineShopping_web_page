from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("mypage/", views.mypage, name="testpages/mypage"),
    # path("logout/", views.logout, name="logout"),
    # path("callback/", views.callback, name="callback"),
]