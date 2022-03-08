from django.urls import path
from . import views

urlpatterns = [
    path('school_list/',views.school_list, name='school_list'),
    path('school_detail/',views.school_detail, name='school_detail'),
    ]