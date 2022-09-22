from functools import wraps
from math import ceil
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.db.transaction import atomic
# from django.contrib.auth.decorators import login_required
from .models import Post, Content

import simplejson
import datetime

from message import Message

# 访问前需登陆：
    # 方法一 path出直接使用login_required(Post_view.as_view())
    # 缺点： 所有方法都必须要登录验证
    # wrapper = post(self, required)
# def login_required(method):
#     @wraps(method)
#     def wrapper(request, *args, **kwargs):
#         print("*"*30)
#         print(request, "\n", *args, "\n", **kwargs)
#         print("*"*30)
#         if request.user.is_authenticated:
#             return method(request, *args, **kwargs)
#         return HttpResponse(status=401)
#     return wrapper

    # 解决办法：path处使用白名单：login_required(["get"])(Post_view.as_view)
def login_required(exclude_method):
    def wrapper_1(view_func):
        @wraps(view_func)
        def wrapper_2(request, *args, **kwargs):
            method = request.method.lower()
            # 若请求方法在白名单内则直接返回视图函数，否则判断认证
            if method in exclude_method:
                return view_func(request, *args, **kwargs)                
            else:
                if request.user.is_authenticated:
                    return view_func(request, *args, **kwargs)                
                return HttpResponse(status=401)
        return wrapper_2
    # FBV时装饰器登录验证
    if callable(exclude_method):
        fn = exclude_method
        exclude_method = []
        return wrapper_1(fn)
    return wrapper_1

# 分页函数简化
def validate(d:dict, name:str, default, type_func, validate_func=lambda x,y:x):
    try:
        value = type_func(d.get(name, default))
        value = validate_func(value, default)
    except:
        value = default
    return value 

class Post_view(View):
    def get(self, request):
        try:
            # 简化代码，抽取重复的部分构建函数
            # try:
            #     page = int(request.GET.get("page", 1))
            #     page = page if page >0 and page < 51 else 1
            # except:
            #     page = 1
            # try:    
            #     size = int(request.GET.get("size", 20))
            #     size = size if size >0 and size<101 else 20
            # except:
            #     size = 20
            # print((type(page), page))
            page = validate(request.GET, 'page', 1, int, validate_func=lambda value, default: value if value >0 and value <51 else default)
            size = validate(request.GET, 'size', 20, int, validate_func=lambda x, y: x if x>0 and x <101 else y)
            start = size*(page-1)
            O = Post.objects
            total = O.count()
            posts = O.order_by('-pk')[start:start+size]
            pages = ceil(total/size)
            print(page,size)
            return JsonResponse({
                'posts':[
                {'id':post.id, 'title':post.title}
                for post in posts
                ],
                'pagination':{
                    'page':page,
                    'size':size,
                    'total':total,
                    'pages': pages
                }
                }
            )
        except Exception as e:
            return HttpResponse("请求方式错误", status=405)
    # 需要提前登录
    # 避开第一个参数self，传入self.post
    # 方法一：path出直接使用login_required(Post_view.as_view())
    def post(self, request):
        try:
            body = simplejson.loads(request.body)
            print(body)
            title = body["title"]
            c = body["content"]
            post = Post(title=title)
            content = Content()
            post.postdate = datetime.datetime.now(
                datetime.timezone(datetime.timedelta(hours=8))
            )
            post.author = request.user
            content.content = c
            with atomic():
                post.save()
                content.post = post
                content.save()
            return JsonResponse({"post":{
                "id":post.id
            }})
        except Exception as e:
            return JsonResponse(Message.BAD_REQUEST)

@login_required
def get_post(request):
    return HttpResponse("FBV  function require_login", status=200)