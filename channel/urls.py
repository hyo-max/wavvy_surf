from django.urls import path
from . import views

urlpatterns = [
    path('channel_list/',views.channel_list, name='channel_list'),
    path('channel_detail/<int:video_id>',views.channel_detail, name='channel_detail'),
    ]