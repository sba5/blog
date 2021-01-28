from django.shortcuts import render
from django.http.response import HttpResponse
from images.models import Photo

# Create your views here.

def index(req, res_data):
    print('=================')
    print(res_data)
    print('=================')
    photos = Photo.objects.all()
    imglist = []
    for photo in reversed(photos):
        imglist.append(str(photo.image))
        print(imglist)

    for i in range(0, 3):
        res_data[f'img{i}'] = 'http://27.96.131.103:8000/media/'+imglist[i]
    # for photo in reversed(photos):
    #     i=0
    #     imgname = str(photo.image)
    #     res_data[f'img{i}'] = 'http://27.96.131.103:8000/media/'+imgname
    #     print(f'img{i}','=',res_data[f'img{i}'])
    #     i=i+1
    #     if i==3:
    #         break
    # res_data['img0'] = 'http://27.96.131.103:8000/media/images/0.png'

    
    return render(req, 'index.html', res_data)