from django.contrib import admin
from .models import Category , ForcastData, Food,Surfschool,Accommodation,Coveniences,Weather
# Register your models here.
admin.site.register(Category)
admin.site.register(ForcastData)
admin.site.register(Food)
admin.site.register(Surfschool)
admin.site.register(Accommodation)
admin.site.register(Coveniences)
admin.site.register(Weather)