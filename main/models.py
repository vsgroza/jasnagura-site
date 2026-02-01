from django.db import models

from django.db import models

# Модель для Новостей/Мероприятий
class Event(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    date = models.DateField("Дата проведения")

    # НОВОЕ ПОЛЕ:
    image = models.ImageField("Фото (внутри новости)", upload_to='events/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['-date']

# Модель для Галереи
class GalleryImage(models.Model):
    title = models.CharField("Подпись (необязательно)", max_length=100, blank=True)
    image = models.ImageField("Фотография", upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Галерея"


# Модель для общих настроек сайта (фон, заголовки)
from django.db import models


# Остальные модели (Event, GalleryImage и т.д.) оставь как есть,
# замени ТОЛЬКО класс SiteSettings на этот:

class SiteSettings(models.Model):
    # Фон шапки
    hero_image = models.ImageField(
        "Фон главной шапки",
        upload_to='site_settings/',
        help_text="Загрузите фото высокого качества (1920x1080)"
    )

    # НОВОЕ ПОЛЕ: Фото для блока "О нас"
    about_image = models.ImageField(
        "Фото в блоке 'О нас'",
        upload_to='site_settings/',
        blank=True,
        null=True,
        help_text="Фото рядом с текстом 'История и Миссия'"
    )

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Общие настройки (Фон, О нас)"



# Модель для сообщений с сайта
class ContactMessage(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата получения", auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "Сообщение с сайта"
        verbose_name_plural = "Входящие сообщения"
        ordering = ['-created_at'] # Свежие сверху


# 5. Онлайн Тесты (Интеграция с Online Test Pad)
class OnlineTest(models.Model):
    title = models.CharField("Название теста", max_length=200)
    # Сюда будем вставлять код, который дает Online Test Pad
    embed_code = models.TextField("Код вставки (Widget)", help_text="Вставьте сюда код Iframe или Script из Online Test Pad")
    is_active = models.BooleanField("Показывать на сайте", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Онлайн тест"
        verbose_name_plural = "Онлайн тесты"