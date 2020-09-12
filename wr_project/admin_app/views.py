from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home")

def login(request):
    return HttpResponse("login")

def signout(request):
    return HttpResponse("Signout")