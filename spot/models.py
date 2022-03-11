from django.db import models
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
        return reverse('spot_list',kwargs={'pk':self.pk})

class ForcastData(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 50)
    desc = models.TextField(verbose_name='설명',max_length = 200)
    img =  models.ImageField(upload_to='spot_pics')

    food_tag = models.ManyToManyField('Food',blank=True,related_name='food')
    surfshool_tag = models.ManyToManyField('Surfschool',blank=True,related_name='surfschool')
    accommodation_tag = models.ManyToManyField('Accommodation',blank=True,related_name='accommodation')
    coveniences_tag = models.ManyToManyField('Coveniences',blank=True,related_name='coveniences')

    lat = models.FloatField(max_length = 100, null=True,blank=True)
    lng = models.FloatField(max_length = 100, null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['category']
        verbose_name_plural = 'spot스팟정보'
        
    def get_absolute_url(self):
        return reverse('spot_detail',kwargs={'pk':self.pk})

class Food(models.Model):                           #맛집
    image = models.ImageField(upload_to='food')
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 50)
    option = models.CharField(max_length = 50)
    phone_number = models.CharField(verbose_name='전화번호',max_length = 50, null=True,blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '맛집'

class Surfschool(models.Model):                         #서핑스쿨
    surfschool_image = models.ImageField(upload_to='surfschool')
    surfschool_title = models.CharField(max_length = 50)
    surfschool_subtitle = models.CharField(max_length = 50)
    surfschool_option = models.CharField(max_length = 50)
    surfschool_number = models.CharField(verbose_name='전화번호',max_length = 50, null=True,blank=True)
    def __str__(self):
        return self.surfschool_title

    class Meta:
        verbose_name_plural = '서핑스쿨'

class Accommodation(models.Model):                         #숙박시설
    accommodation_image = models.ImageField(upload_to='accommodation')
    accommodation_title = models.CharField(max_length = 50)
    accommodation_subtitle = models.CharField(max_length = 50)
    accommodation_option = models.CharField(max_length = 50)
    accommodation_number = models.CharField(verbose_name='전화번호',max_length = 50, null=True,blank=True)
    def __str__(self):
        return self.accommodation_title

    class Meta:
        verbose_name_plural = '숙박시설'


class Coveniences(models.Model):                        #편의시설
    coveniences_image = models.ImageField(upload_to='coveniences')
    coveniences_title = models.CharField(max_length = 50)
    coveniences_subtitle = models.CharField(max_length = 50)
    coveniences_option = models.CharField(max_length = 50)
    coveniences_number = models.CharField(verbose_name='전화번호',max_length = 50, null=True,blank=True)
    def __str__(self):
        return self.coveniences_title

    class Meta:
        verbose_name_plural = '편의시설'

class Weather(models.Model):
    spot = models.ForeignKey(ForcastData, on_delete=models.CASCADE, null=True, related_name='spot') # 관계 설정

    airTemperature = models.FloatField(null=True,blank=True)           #섭씨 온도 
    waterTemperature =  models.FloatField(null=True,blank=True)        #물 섭씨 온도
    precipitation = models.FloatField(null=True,blank=True)            #kg / m²의 평균 강수량
    cloudCover = models.FloatField(null=True,blank=True)               #구름 농도

    waveDirection = models.FloatField(null=True,blank=True)            #파도 방향
    waveHeight = models.FloatField(null=True,blank=True)               #파도 높이
    wavePeriod = models.FloatField(null=True,blank=True)               #파도 주기

    windDirection = models.FloatField(null=True,blank=True)            #바람 방향
    gust = models.FloatField(null=True,blank=True)                     #초당 미터 바람속도

    weather_icon = models.CharField(max_length = 50,null=True,blank=True)              #날씨아이콘

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'weather'