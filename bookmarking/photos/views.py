import json

from django.http import JsonResponse
from django.shortcuts import render

from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photos/photo_list.html', {'photos': photos})

def add_bookmark(request):
    if request.method == 'POST':
        photo_id = json.loads(request.body).get('photo_id')
        bookmarks = request.session.get('bookmarks', [])
        if photo_id not in bookmarks:
            bookmarks.append(photo_id)
        request.session['bookmarks'] = bookmarks
        return JsonResponse({'status': 'ok'})

def remove_bookmark(request):
    if request.method == 'POST':
        photo_id = json.loads(request.body).get('photo_id')
        bookmarks = request.session.get('bookmarks', [])
        if photo_id in bookmarks:
            bookmarks.remove(photo_id)
        request.session['bookmarks'] = bookmarks
        return JsonResponse({'status': 'ok'})