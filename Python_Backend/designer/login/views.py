from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.middleware import csrf
# Create your views here.


def login_designer(request):
    if request.method == 'GET':
        token = get_or_create_csrf_token(request)
        return HttpResponse(token)
    elif request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse(request, status=200)
        else:
            return HttpResponse(request, status=400)


def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_token()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token
#     localhost:8000/login/post/login
