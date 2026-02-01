from django.contrib import admin
from django.utils.html import mark_safe  # Позволяет выводить HTML (картинки) в админке
from .models import Event, GalleryImage, SiteSettings, ContactMessage, OnlineTest


# 1. Настройка для Мероприятий (Новости)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')  # Какие столбцы показывать
    search_fields = ('title', 'description')  # Строка поиска
    list_filter = ('date',)  # Фильтр справа


# 2. Настройка для Галереи (С картинками!)
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    # Показываем: Превью, Заголовок, Имя файла, Дату
    list_display = ('image_preview', 'title', 'image', 'uploaded_at')
    readonly_fields = ('image_preview',)  # Чтобы превью было и внутри карточки

    # Функция, которая рисует маленькую картинку
    def image_preview(self, obj):
        if obj.image:
            # mark_safe говорит Django: "Это безопасный HTML, нарисуй его"
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; border-radius: 5px;">')
        return "Нет фото"

    image_preview.short_description = "Миниатюра"


# 3. Настройка для Шапки сайта (Фон)
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'hero_image')

    def image_preview(self, obj):
        if obj.hero_image:
            return mark_safe(f'<img src="{obj.hero_image.url}" style="max-height: 100px; border-radius: 5px;">')
        return "Нет фото"

    image_preview.short_description = "Текущий фон"


# 4. Настройка для Сообщений (Почта)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    ordering = ('-created_at',)

@admin.register(OnlineTest)
class OnlineTestAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')

