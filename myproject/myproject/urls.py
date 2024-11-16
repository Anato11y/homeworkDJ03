from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Маршруты для приложения main
    path('news/', include('news.urls')),  # Маршруты для приложения news
]

