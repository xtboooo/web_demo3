from django.shortcuts import render, HttpResponse, redirect
from users.models import User
from django.http import JsonResponse
from django.views import View


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        import json
        req_dict = json.loads(request.body)
        username = req_dict.get('username')
        password = req_dict.get('username')
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)
        print(f'username:{username} password:{password}')
        # return redirect('/login/')
        return HttpResponse('注册成功')


def login(request):
    """登陆 View 视图函数"""
    username = request.session.get('username')
    if username:
        return HttpResponse(f'{username} 用户已登陆')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            if remember != 'true':
                request.session.set_expiry(0)
            response = JsonResponse({'message': 'login success'})
            return response


def user_info(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'})
    else:
        res_data = {
            'id': user.id,
            'name': user.username,
            'gender': user.gender,
            'age': user.age,
            'mobile': user.mobile,
        }
    return JsonResponse(res_data)


class LoginView(View):
    """登陆类视图"""

    def get(self, request):
        username = request.session.get('username')
        if username:
            return HttpResponse(f'{username} 用户已登陆')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            if remember != 'true':
                request.session.set_expiry(0)
            response = JsonResponse({'message': 'login success'})
            return response
