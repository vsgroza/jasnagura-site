from django.db import models

from django.db import models

# Модель для Новостей/Мероприятий
class Event(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    date = models.DateField("Дата проведения")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['-date'] # Сортировка: сначала новые

# Модель для Галереи
class GalleryImage(models.Model):
    title = models.CharField("Подпись (необязательно)", max_length=100, blank=True)
    image = models.ImageField("Фотография", upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Галерея"


# Модель для общих настроек сайта (фон, заголовки)
class SiteSettings(models.Model):
    hero_image = models.ImageField("Фон главной шапки", upload_to='site_settings/',
                                   help_text="Загрузите фото высокого качества (1920x1080)")

    class Meta:
        verbose_name = "Настройки шапки"
        verbose_name_plural = "Настройки шапки"

    def __str__(self):
        return "Настройки главной страницы"

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


