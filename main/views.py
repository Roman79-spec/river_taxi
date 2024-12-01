import requests
from django.shortcuts import render
from django.http import JsonResponse

def main_page(request):
    data = {
        'title': 'HaronMoscov',
    }
    return render(request, 'main/main_page.html', data)

def about(request):
    return render (request, 'main/about_us.html')
