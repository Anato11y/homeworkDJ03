from django.contrib import admin
from .models import NewsPost

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    search_fields = ('title', 'short_description', 'author__username')

admin.site.register(NewsPost, NewsPostAdmin)

