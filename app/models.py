from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User 
# Create your models here.

class Item(models.Model):
    text = models.TextField(default='')
    times = models.CharField(max_length=50)

class UserProfile(models.Model):  
    user=models.OneToOneField(User,unique=True,verbose_name=('用户'))
    phone=models.CharField(max_length=20)

 
class Blog(models.Model):
    """
    博客
    """
    Id = models.AutoField(auto_created = True, primary_key = True,serialize = False,verbose_name = 'ID')
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)


class Comment(models.Model):
    """
    评论
    """
 
    blog = models.ForeignKey(Blog, verbose_name='博客')
 
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)
 
    created = models.DateTimeField('发布时间', auto_now_add=True)