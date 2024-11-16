from django.db import models
from django.contrib.auth.models import User  # Для работы с пользователями

class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=50)  # Заголовок новости
    short_description = models.CharField('Краткое описание новости', max_length=200)  # Краткое описание
    text = models.TextField('Полный текст новости')  # Полный текст новости
    pub_date = models.DateTimeField('Дата публикации')  # Дата публикации
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')  # Автор новости

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
