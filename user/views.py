from functools import wraps

from django.http import HttpResponse, HttpRequest, JsonResponse
# from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
# from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore

import simplejson
from message import Message

# Create your views here.
def index(request:HttpRequest):
    # print(request.path)
    # print(request.GET)
    # print(request.POST)
    # print(request.method)
    # print(request.COOKIES)
    # print(request.body)
    # print(request.content_type)
    # print(Message.BAD_REQUEST)
    try:
        body = simplejson.loads(request.body)
        username = body["username"]
        print(body)
        count = User.objects.filter(username=username).count()
        if count > 0:
            return JsonResponse(Message.USER_EXIST, status=200)
            # return HttpResponse(Message.USER_EXIST)
        user = User.objects.create_user(username=username, email=body["email"], password=body["password"],)
        print(type(user))
        return JsonResponse({}, status=200)
    except Exception as e:
        return JsonResponse(Message.BAD_REQUEST, status=200)
    
@require_POST
def user_login(request):
    try:
        body = simplejson.loads(request.body)
        # username = body["username"]
        # passwd = body["password"]
        # print("body:{}".format(body))
        user = authenticate(**body) # user是和数据库对应的真实的用户，is_authencated方法返回的是True
        # print(type(user), user)
        # print("="*30)
        # if user:
            # print(type(user), user, "\n","-"*30)
        # print(type(request.user), request.user) # request.user 是一个匿名用户，is_authencated方法返回的是FALSE
        if user:
            login(request, user) # 绑定user和request.user
            session:SessionStore = request.session
            # session.set_expiry(60) # 设置session的过期时间
            # print(type(request.session), "\n ", "="*30)
            session["userinfo"] ={
                "id": request.user.id,
                "username": request.user.username
            }
            """
            1. 各种后台习惯上通过request.session来获取session的值
            2. request.user = user : 将真实的用户绑定给request, 不在是原来默认的匿名用户
            """
            # print(*request.session.items(), sep="\n")
            return HttpResponse("success login", status=204)
        return JsonResponse(Message.INVALID_USERNAME_OR_PASSWD, status=200)
    except Exception as e:
        # return HttpResponse(status=200)
        return JsonResponse(Message.BAD_REQUEST, status=200)

# 自定义登录装饰器：用户登录后才能访问
def login_required(viewfunc):
    @wraps(viewfunc)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return viewfunc(request, *args, **kwargs)
        return HttpResponse(status=401)
    return wrapper



@login_required
# @login_required(login_url="/user/login")
def user_logout(request:HttpRequest):
    # print(type(request.user ),request.user)
    # logout(request) # 会彻底清除sessionid.移除request.user ；清除django_session记录(无痕浏览器)
    print("user view logout in", "+"*30)
    print(request.user)
    print(*request.session.items(), sep="\n")
    print("user view logout out", "+"*30)

    return HttpResponse("看见啦", status=200)

# from django.contrib.sessions.middleware import SessionMiddleware
# from django.contrib.auth.middleware import AuthenticationMiddleware  # 依赖session的中间件

class SimpleMiddleware1:
    def __init__(self, get_response): # 一次性的中间件对象初始化使用
        self.get_response = get_response
    
    def __call__(self, request) :

        # 每一个中间件返回response之前调用， 对request做处理
        print("*"*30, "\n",  "before get_response", "process_request")
        print(request.session.items())
        print(request.user)
        # if request.user.is_authenticated:
        #     response = self.get_response(request)  # 调用下一个,向内调用view函数，返回的response是view函数的response
        #     # 可以对response 和 request 做处理
        #     print("="*30, "\n",  "after get_response")
        #     print(response)
        #     return response
        # return HttpResponse("提前结束",status=402)

        response = self.get_response(request)  # 调用下一个,向内调用view函数，返回的response是view函数的response
        
        print("="*30, "\n",  "after get_response", "process_response")
        print(response)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("SimpleMiddleware1 process_view start","-"*30)
        print(view_func)
        print("SimpleMiddleware1 process_view stop","-"*30)
        # return HttpResponse("Process1_view故意的",status=404) # 不会向后调用，从此处返回

class SimpleMiddleware2:
    def __init__(self, get_response): # 一次性的中间件对象初始化使用
        self.get_response = get_response
    
    def __call__(self, request) :

        # 每一个中间件返回response之前调用， 对request做处理
        print("2*"*30, "\n",  "before get_response", "process_request")
        print(request.session.items())
        print(request.user)
        # if request.user.is_authenticated:
        #     response = self.get_response(request)  # 调用下一个,向内调用view函数，返回的response是view函数的response
        #     # 可以对response 和 request 做处理
        #     print("="*30, "\n",  "after get_response")
        #     print(response)
        #     return response
        # return HttpResponse("提前结束",status=402)

        response = self.get_response(request)  # 调用下一个,向内调用view函数，返回的response是view函数的response
        
        print("2="*30, "\n",  "after get_response", "process_response")
        print(response)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("SimpleMiddleware2 process_view start","2-"*30)
        print(view_func)
        print("SimpleMiddleware2 process_view stop","2-"*30)
        # return HttpResponse("process_view2故意的",status=404) # 不会向后调用，从此处返回