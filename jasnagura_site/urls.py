from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
# Новый путь для AI
    path('api/ask_ai/', views.ai_proxy, name='ask_ai'),
path('api/contact/', views.save_contact_message, name='save_contact')
]

# Эта магическая строка позволяет видеть загруженные фото при разработке
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)