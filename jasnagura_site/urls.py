from django.contrib import admin
# ВНИМАНИЕ: Добавили 'include' в импорт ниже
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from main import views

# 1. Ссылки, которые НЕ зависят от языка (Технические)
urlpatterns = [
    path('admin/', admin.site.urls),

    # --- ВОТ ЭТА СТРОКА ИСПРАВЛЯЕТ ОШИБКУ ---
    # Она подключает встроенную логику переключения языков
    path('i18n/', include('django.conf.urls.i18n')),
    # ----------------------------------------

    path('api/ask_ai/', views.ask_ai, name='ask_ai'),
    path('api/contact/', views.save_contact_message, name='save_contact'),
]

# 2. Ссылки, которые БУДУТ переводиться (добавится /ru/ или /pl/)
urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('test/<int:test_id>/', views.test_detail, name='test_detail'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
)

# 3. Для картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)