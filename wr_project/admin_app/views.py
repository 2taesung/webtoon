from django.shortcuts import render
from django.http import HttpResponse
from admin_app.models import action, romance, fantasy


# Create your views here.

#model.py에서 만든 더미 데이터 이용한 action_after_ranking 변수
def home(request):
    action_after_ranking = action.objects.all().order_by('after_ranking')[:5]
    context = {'action_after_ranking': action_after_ranking}
    return render(request, 'admin_app/home.html', context)

def login(request):
    return HttpResponse("login")

def signout(request):
    return HttpResponse("Signout")

def signup(request):
    return HttpResponse("Signup")

def bulletinboard(request):
    return HttpResponse("bulletinboard")