from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Photo

# Create your views here.

def photo(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        content = req.POST.get('content')
        imgs = req.FILES.get('imgs')

        photo = Photo(
            title = title,
            content = content,
            image = imgs,
        )
        photo.save()

        res_data = {}
        photos = Photo.objects.all().order_by('-id')
        imglist = []
        titlelist = []
        for photo in photos:
            imglist.append(photo.image)
            titlelist.append(photo.title)
             
        for i in range(0, 10):
            res_data[f'img{i}'] = 'http://27.96.131.103:8000/media/'+str(imglist[i])
            res_data[f'title{i}'] = str(titlelist[i])

        # res_data = {}
        # # res_data = {}
        # # res_data['res'] = '회원가입을 축하드립니다!'
        # # print(req.POST['username'])
        # res_data['title0'] = title
        # print(str(imgs))
        # print(title)
        # res_data['img0'] = 'http://27.96.131.103:8000/media/images/'+str(imgs)
        return render(req, 'photo.html', res_data)


    res_data = {}
    photos = Photo.objects.all().order_by('-id')
    imglist = []
    titlelist = []
    for photo in photos:
        imglist.append(photo.image)
        titlelist.append(photo.title)    

    for i in range(0, 10):
        res_data[f'img{i}'] = 'http://27.96.131.103:8000/media/'+str(imglist[i])
        res_data[f'title{i}'] = str(titlelist[i])
    
    return render(req, 'photo.html', res_data) 