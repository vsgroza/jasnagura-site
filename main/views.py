import json
import os
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Event, GalleryImage, SiteSettings, ContactMessage


def index(request):
    events = Event.objects.all()
    gallery_images = GalleryImage.objects.all()
    settings = SiteSettings.objects.last()

    context = {
        'events': events,
        'gallery_images': gallery_images,
        'settings': settings,
    }
    return render(request, 'main/index.html', context)


# --- AI ФУНКЦИЯ ---
@csrf_exempt
def ask_ai(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_prompt = data.get('prompt', '')

            # === КЛЮЧ ===
            # Вставь свой ключ AIza... (если он там уже есть - не трогай)
            api_key = os.environ.get("GEMINI_API_KEY", "ТВОЙ_КЛЮЧ_AIza...")

            genai.configure(api_key=api_key)

            # === ВАЖНОЕ ИЗМЕНЕНИЕ ===
            # Используем актуальную модель из твоего списка 2026 года
            model = genai.GenerativeModel('gemini-2.5-flash')

            # Спрашиваем у AI
            response = model.generate_content(user_prompt)

            return JsonResponse({'text': response.text})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

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