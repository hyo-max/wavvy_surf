from django.db import models
from django.utils import timezone
from django.shortcuts import resolve_url
from django.urls import reverse

class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='sub_categories')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('school_list',kwargs={'pk':self.pk})


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 50)
    desc = models.TextField(verbose_name='설명',max_length = 200)
    address = models.CharField(verbose_name='주소',max_length = 50)
    phone_number = models.CharField(verbose_name='전화번호',max_length = 50)
    link = models.URLField(verbose_name='홈페이지',blank=True, null=True)
    img =  models.ImageField(upload_to='school_pics')

    parking = models.BooleanField(verbose_name='주차')
    reservation = models.BooleanField(verbose_name='예약')
    wifi = models.BooleanField(verbose_name='와이파이')
    shower = models.BooleanField(verbose_name='샤워')
    amenities = models.BooleanField(verbose_name='어메니티')

    lat = models.FloatField(verbose_name='위도',max_length = 100)
    lng = models.FloatField(verbose_name='경도',max_length = 100)

    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['category']
        
    def get_absolute_url(self):
        return reverse('school-detail',kwargs={'pk':self.pk})
