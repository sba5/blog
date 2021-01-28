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

def diary(req):
    if req.method == 'POST':
        diary = req.POST.get('diary')

        diary = Diary(
            diary = diary,
        )
        diary.save()

        res_data = {}
        diaries = Diary.objects.all().order_by('-id')
        diarylist = []
        for diary in diaries:
            diarylist.append(diary.diary)
             
        for i in range(0, 10):
            res_data[f'diary{i}'] = str(diarylist[i])

        # res_data = {}
        # # res_data = {}
        # # res_data['res'] = '회원가입을 축하드립니다!'
        # # print(req.POST['username'])
        # res_data['title0'] = title
        # print(str(imgs))
        # print(title)
        # res_data['img0'] = 'http://27.96.131.103:8000/media/images/'+str(imgs)
        return render(req, 'photo.html', res_data)


    diary = req.POST.get('diary')

    diary = Diary(
        diary = diary,
    )
    diary.save()

    res_data = {}
    diaries = Diary.objects.all().order_by('-id')
    diarylist = []
    for diary in diaries:
        diarylist.append(diary.diary)
             
    for i in range(0, 10):
        res_data[f'diary{i}'] = str(diarylist[i])
    
    return render(req, 'photo.html', res_data) 