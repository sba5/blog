from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
from pages.views import index

# Create your views here.

# def index(req):
#     return HttpResponse("<h1>hello</h1>")


# def index(req):
#     return render(req, 'index.html')

def login(req):
    if req.method == 'POST':
        userid = req.POST.get('userid')
        userpw = req.POST.get('userpassword')

        res_data = {}

        members = Members.objects.all() #Members에 있는 모든 객체를 불러와 members에 저장
        for member in members:
            if userid == member.userid:
                if userpw == member.userpassword:
                    res_data['res'] = member.username
                    # res_data['pid'] = member.id
                    print('member pid : ', member.id)
                    print('로그인 성공')
                    #return render(req, 'index.html', res_data)
                    return index(req, res_data)

        res_data['res'] = '아이디가 존재하지 않거나 비밀번호가 틀렸습니다.'
        return render(req, 'login.html', res_data)
        
        # print(req.POST['userid'])


    return render(req, 'login.html')

def signup(req):
    if req.method == 'POST':
        userid = req.POST.get('userid')
        userpw = req.POST.get('userpassword')
        usergender = req.POST.get('usergender')
        username = req.POST.get('username')
        useremail = req.POST.get('useremail')
        userphone = req.POST.get('userphone')
        useraddress = req.POST.get('useraddress')
        member = Members(
            userid = userid,
            userpassword = userpw,
            username = username,
            usergender = usergender,
            useremail = useremail,
            userphone = userphone,
            useraddress = useraddress,
        )
        
        member.save()
        # res_data = {}
        # res_data['res'] = '회원가입을 축하드립니다!'
        print(req.POST['username'])
        return render(req, 'login.html')

        
    return render(req, 'signup.html')
