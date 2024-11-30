import requests
from django.shortcuts import render
from django.http import JsonResponse

def main_page(request):
    return render(request, 'main/main_page.html')
