from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
    path('add/', views.add_news, name='add_news'),  # Добавление новости
]
