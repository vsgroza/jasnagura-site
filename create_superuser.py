import os
import django

# Настройка окружения Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jasnagura_site.settings")
django.setup()

from django.contrib.auth.models import User

# Настройки админа (МОЖЕШЬ ПОМЕНЯТЬ ПАРОЛЬ ЗДЕСЬ)
USERNAME = 'admin'
EMAIL = 'admin@example.com'
PASSWORD = 'admin_password_123'  # <--- Временный пароль

if not User.objects.filter(username=USERNAME).exists():
    print(f"Создаю суперпользователя {USERNAME}...")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Суперпользователь создан!")
else:
    print("Суперпользователь уже существует.")