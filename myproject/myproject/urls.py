from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),  # Выход из системы
    path('', include('main.urls')),  # Главная страница
    path('news/', include('news.urls')),  # Новости
]

