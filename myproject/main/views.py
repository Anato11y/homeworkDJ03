from django.shortcuts import render
from news.models import NewsPost  # Импорт модели из приложения news
def index(request):
    return render(request, 'main/index.html')
def home(request):
    news = NewsPost.objects.all()  # Получаем все новости
    return render(request, 'news/news.html', {'news': news})