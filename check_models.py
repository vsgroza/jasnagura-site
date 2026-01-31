import google.generativeai as genai
import os

# === ВСТАВЬ СЮДА СВОЙ КЛЮЧ ===
api_key = "AIzaSyAwz02DmeSWnUfPrftMb882AtWQ6tkjGhk"

genai.configure(api_key=api_key)

print("--- СПИСОК ДОСТУПНЫХ МОДЕЛЕЙ ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Ошибка: {e}")