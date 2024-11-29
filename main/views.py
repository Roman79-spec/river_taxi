import requests
from django.shortcuts import render
from django.http import JsonResponse

#API-ключ 2GIS
API_KEY = '0290df9b-589c-4daa-bb5b-13508b57a8b9'

def calculate_route(request):
    if request.method == 'POST':
        start = request.POST.get('start')  # Откуда
        end = request.POST.get('end')  # Куда

        # Отправка запроса в Distance Matrix API 2GIS
        url = "https://api.2gis.ru/distance/v1.0/computeMatrix"
        
        params = {
            'key': API_KEY,
            'points': f"{start},{end}"
        }
        
        response = requests.get(url, params=params)
        data = response.json()

        # Извлекаем расстояние и время из ответа
        distance = data.get('matrix', [{}])[0].get('distance', 'Неизвестно')
        duration = data.get('matrix', [{}])[0].get('duration', 'Неизвестно')

        return render(request, 'main/index1.html', {'distance': distance, 'duration': duration, 'start': start, 'end': end})

    return render(request, 'main/index1.html')
