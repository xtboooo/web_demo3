from django.shortcuts import render, HttpResponse, redirect
from users.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)
        print(f'username:{username} password:{password}')
        return redirect('/login/')


def login(request):
    """登陆 View 视图函数"""
    return render(request, 'login.html')

