import json
import os
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Event, GalleryImage, SiteSettings, ContactMessage  # Импортируем наши модели


def index(request):
    events = Event.objects.all()
    gallery_images = GalleryImage.objects.all()

    # Берем ПОСЛЕДНЮЮ загруженную настройку
    settings = SiteSettings.objects.last()

    context = {
        'events': events,
        'gallery_images': gallery_images,
        'settings': settings,  # <--- Передаем настройки в шаблон
    }

    return render(request, 'main/index.html', context)

# --- НАСТРОЙКА AI ---
# Получаем ключ из настроек сервера (Render)
api_key = os.environ.get("GEMINI_API_KEY")

# Если на сервере ключа нет, используем запасной (ваш локальный)
if not api_key:
    api_key = "AIzaSyB9FCZB3Mv0yUMe0hNhLaGmTTihX1OGPCg"

# Настраиваем AI
genai.configure(api_key=api_key)

@csrf_exempt # Отключаем строгую проверку безопасности для упрощения (только для этой функции)
def ai_proxy(request):
    if request.method == 'POST':
        try:
            # Получаем данные из запроса (то, что прислал JavaScript)
            data = json.loads(request.body)
            user_prompt = data.get('prompt', '')

            # Выбираем модель
            model = genai.GenerativeModel('gemini-1.5-flash')

            # Спрашиваем у AI
            response = model.generate_content(user_prompt)

            # Возвращаем ответ обратно на сайт
            return JsonResponse({'text': response.text})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def save_contact_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Создаем запись в базе
            ContactMessage.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                message=data.get('message')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)