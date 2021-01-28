from django.shortcuts import render
from django.http.response import HttpResponse
from images.models import Photo

# Create your views here.

def index(req, res_data):
    print('=================')
    print(res_data)
    print('=================')
    photos = Photo.objects.all()
    for photo in reversed(photos):
        i=0
        print(photo.content)
        i=i+1
        if i==1:
            break
    # res_data['recent_img']
    return render(req, 'index.html', res_data)