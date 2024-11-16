from django.http import request
from django.shortcuts import render, redirect
from .forms import NewsPostForm  # Форма для добавления новости
from django.contrib.auth.decorators import login_required
from .models import NewsPost  # Импорт модели для работы с новостями
@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user  # Указываем текущего пользователя как автора
            news.save()
            return redirect('news_home')  # Перенаправление на список новостей
    else:
        form = NewsPostForm()
    return render(request, 'news/add_news.html', {'form': form})
def home(request):
       news = NewsPost.objects.all()  # Получаем все новости
       return render(request, 'news/news.html', {'news': news})