from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.challenge_list, name="challenges_list"),
]
