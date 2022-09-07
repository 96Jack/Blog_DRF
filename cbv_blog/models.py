from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    class Meta:
        db_table = "post"
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, unique=False)
    postdate = models.DateTimeField(null=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __repr__(self) -> str:
        return "<Post: {} {} {}>".formmat(self.id, self.title, self.postdate)
    
    __str__ = __repr__

class Content(models.Model):
    class Meta:
        db_table = "content"
    post = models.OneToOneField(Post, on_delete=models.PROTECT, primary_key=True)
    content = models.TextField(null=True)

    def __repr__(self) -> str:
        return "<Content:{} {}>".format(self.pk, self.content[:20])

    __str__ = __repr__
