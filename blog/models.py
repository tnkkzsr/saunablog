from django.db import models

#投稿機能のカテゴリーに関するモデル
class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name

#投稿機能のタグに関するモデル
class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name
from django.urls import reverse_lazy

#投稿機能の本体のモデル
class Post(models.Model):

    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])


    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)
    
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
        
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
        
    body = models.TextField(
        blank=True,
        null=False)
        
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)
        
    tags = models.ManyToManyField(
        Tag,
        blank=True)

    def __str__(self):
        return self.title


#ここから、サインアップ機能
from django.db import models
from django.contrib.auth.models import AbstractUser

#AbstractUserを継承した独自のユーザーモデルを作る
class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
