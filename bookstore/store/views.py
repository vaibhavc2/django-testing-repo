from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'store/index.html')

def set_language(request):
    response = HttpResponse("Language set")
    response.set_cookie('lang', request.GET.get('lang'), max_age=30*24*60*60) # Set cookie for 30 days
    return response