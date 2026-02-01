import json
import os
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import Event, GalleryImage, SiteSettings, ContactMessage, OnlineTest


def index(request):
    events = Event.objects.all()
    gallery_images = GalleryImage.objects.all()
    settings = SiteSettings.objects.last()
    online_tests = OnlineTest.objects.filter(is_active=True)

    context = {
        'events': events,
        'gallery_images': gallery_images,
        'settings': settings,
        'online_tests': online_tests,
    }
    return render(request, 'main/index.html', context)


# --- AI ФУНКЦИЯ (БЕЗОПАСНАЯ) ---
@csrf_exempt
def ask_ai(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_prompt = data.get('prompt', '')

            # === БЕЗОПАСНОЕ ПОЛУЧЕНИЕ КЛЮЧА ===
            # Мы больше НЕ пишем ключ в кавычках здесь!
            # Python возьмет его из настроек Render или PyCharm.
            api_key = os.environ.get("GEMINI_API_KEY")

            if not api_key:
                return JsonResponse({'error': 'API Key not found. Check environment variables.'}, status=500)

            genai.configure(api_key=api_key)

            # Используем актуальную модель
            model = genai.GenerativeModel('gemini-2.5-flash')

            response = model.generate_content(user_prompt)
            return JsonResponse({'text': response.text})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)


# НОВАЯ ФУНКЦИЯ: Страница конкретного теста
def test_detail(request, test_id):
    # Ищем тест по ID, если нет - ошибка 404
    test = get_object_or_404(OnlineTest, id=test_id)

    context = {
        'test': test
    }
    return render(request, 'main/test_detail.html', context)

# --- СООБЩЕНИЯ ---
@csrf_exempt
def save_contact_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ContactMessage.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                message=data.get('message')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)