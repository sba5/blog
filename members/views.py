from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

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
                    return render(req, 'index.html', res_data)
                else:
                    print("비밀번호가 틀림")
                    res_data['res'] = '비밀번호가 틀림'
            else:
                res_data['res'] = '존재하지 않는 아이디입니다.'
        
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
        res_data = {}
        res_data['res'] = '회원가입을 축하드립니다!'
        print(req.POST['username'])
        return render(req, 'signup.html', res_data)

        
    return render(req, 'signup.html')
