from django.db import models
from django.utils import timezone
from accounts.models import User
from django.shortcuts import resolve_url
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='sub_categories')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('commu_list',kwargs={'pk':self.pk})


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = timezone.now)
    body = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['category']
        
    def get_absolute_url(self):
        return reverse('commu-detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments') # 관계 설정
    comment_date = models.DateTimeField(default = timezone.now) # 댓글 날짜
    comment_body = models.CharField(max_length=200) # 댓글 내용
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 유저 관계설정
    
    def __str__(self):
        return self.comment_body
        
    class Meta:
        ordering=['id'] # 정렬기준
    