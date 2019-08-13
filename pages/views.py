import random
import datetime
from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 3. >> 로직 <<
    # 4. 해당하는 템플릿 반환
    return render(request, 'pages/index.html')

def hello(request, name):
    context = {'name':name}
    return render(request, 'pages/hello.html',context)

def lotto(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1,46),6))
    # 값을 딕셔너리에 담아서(보통 context라고 부름)
    context ={'lotto': numbers}
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language(DTL) !
    return render(request, 'pages/lotto.html',context)

def dinner(request):
    menus =['롯데리아', '편의점도시락', '맘스터치', '응급실떡볶이', '노은각', '피자', '치킨']
    pick = random.choice(menus)
    context = {
        'pick':pick,
        'menus':menus, 
        'users':[],
        'sentence' : 'Life is short. You need python + Django !',
        'datetime_now': datetime.datetime.now(),
        'google_link':'https://www.google.com'
        }
    return render(request, 'pages/dinner.html', context)

def cube(request, num):
    context = {
        'cube': num **3,
        'numbers' : [1,2,3],
        'students': {'지수': '지수야','태수':'태수야'}
        }
    return render(request, 'pages/cube.html',context)

def about(request, name, age):
    context = {'name':name, 'age':age}
    return render(request, 'pages/about.html',context)

def isitgwangbok(request):
    now = datetime.datetime.now()
    if now.month ==8 and now.day ==15:
        result = True
    else:
        result = False
    context ={
        'result':result
    }
    return render(request, 'pages/isitgwangbok.html', context)

def ping(request):
    return render(request,'pages/ping.html')

def pong(request):
    # 사용자가 넘겨주는 값 받아오기
    print(request.GET) # QueryDict
    data = request.GET.get('data')
    context = {
        'data' : data,
    }
    return render(request,'pages/pong.html',context)

def signup(request):
    return render(request,'pages/signup.html')

def signup_result(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    pwd_confirmation = request.POST.get('pwd_confirmation')
    if pwd == pwd_confirmation:
        result = "회원가입을 축하드립니다."
    else:
        result = "비밀번호를 다시 확인해주세요"
    context = {
        'pwd' : pwd,
        'name' : name,
        'username' : username,
        'result' : result
    }
    return render(request,'pages/signup_result.html',context)