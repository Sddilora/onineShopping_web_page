from django.urls import path, include
from . import views

urlpatterns = [
    path("form/", views.product_form, name="testinput/form"),
]