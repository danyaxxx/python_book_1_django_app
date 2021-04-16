"""Определяет схемы URL для learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
]