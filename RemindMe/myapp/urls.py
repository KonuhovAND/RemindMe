from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.email_form_view, name="sender"),
]
