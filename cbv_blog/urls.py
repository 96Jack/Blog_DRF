from django.urls import path

from .views import Post_view, login_required , get_post

urlpatterns = [
# 访问前需登陆：方法一
    # 缺点： 方法在dispatch之前，所有方法都需要认证
    # path("",login_required( Post_view.as_view())),
    # 解决方法： 添加白名单
    # login_required()相当于带参装饰器
    path("", login_required(["get"])(Post_view.as_view())),
    path("get_post/", get_post)
]


