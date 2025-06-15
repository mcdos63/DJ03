from django.contrib import admin
from .models import News_post

@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')  # Отображаемые поля в списке новостей
    list_filter = ('pub_date', 'author')  # Фильтры справа
    search_fields = ('title', 'short_description')  # Поиск по заголовку и краткому описанию