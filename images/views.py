from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Photo

# Create your views here.

def photo(req):
    if req.method == 'POST':
        title = req.POST.get('imgtitle')
        print('============')
        print(req)
        print(title)

    return render(req, 'photo.html') 