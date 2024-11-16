from django.shortcuts import render
from .models import NewsPost

def home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news})

