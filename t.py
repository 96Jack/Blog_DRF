import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blog_DRf.settings")
django.setup()
###############
import datetime

from cbv_blog.models import Post, Content
from django.db.transaction import atomic
from django.contrib.auth.models import User
user = User()
user.id = 1
user.username="t"
user.password="1234"
user.save()
print(user.id)
print(user.pk)
# post=Post()
# print(post.id)
# try:
#     user = User.objects.filter(username='admin')[0]
#     print(user.id,"*"*30)
#     post.id = 5
#     # print(dir(user))
#     # print(user.author_user,"*"*30)
#     post.title = 't55'
#     post.postdate = datetime.datetime.now(
#         datetime.timezone(datetime.timedelta(hours=8))
#     )
#     post.author_id= user.id
#     c = Content()
#     c.content = "内容5"
#     with atomic():
#         post.save()
#         c.post = post
#         c.save()
#     print(post.pk)
# except Exception as e:
#     print(e)
#     print("="*30)