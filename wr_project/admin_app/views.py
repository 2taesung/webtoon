from django.shortcuts import render
from django.http import HttpResponse

class1_students = ['이태성', '김혜란', '송두기', '이윤환']

# Create your views here.
def home(request):
    name = '이태성'
    return render(request, 'home.html', {'username':name})

def login(request):
    return HttpResponse("login")

def signout(request):
    return HttpResponse("Signout")

def result(request):
    # print('🤞', request.POST['username'])
    username = request.POST['username']

    if username in class1_students:
        print('🐱‍🚀 1반의 학생이예요')
    else :
        print('🤷‍♀️ 1반의 학생이 아닙니다')

    return render(request, 'result.html')