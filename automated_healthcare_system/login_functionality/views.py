from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'login_functionality/register.html')


def login(request):
    return render(request, 'login_functionality/login.html')