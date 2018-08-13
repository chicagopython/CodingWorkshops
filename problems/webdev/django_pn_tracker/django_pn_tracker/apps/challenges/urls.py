from django.contrib import admin
from django.urls import path
from . import views

# Learn about django urls:
# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.challenge_list, name="challenges_list"),
    path('add/', views.challenge_add, name='challenges_add'),
    path('<int:id>/', views.challenge_edit, name='challenges_edit'),
    path('<int:id>/delete/', views.challenge_delete, name='challenges_delete'),
]
