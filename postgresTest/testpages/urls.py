from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("mypage/", views.mypage, name="testpages/mypage"),
    # path("add-product/", views.product_list, name="product_list"),
    # path("callback/", views.callback, name="callback"),
]