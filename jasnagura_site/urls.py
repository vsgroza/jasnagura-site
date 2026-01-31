from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views  # Импортируем наши функции

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # Вот эти две строки должны совпадать с названиями в views.py:
    path('api/ask_ai/', views.ask_ai, name='ask_ai'),
    path('api/contact/', views.save_contact_message, name='save_contact'),
]

# Для картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)