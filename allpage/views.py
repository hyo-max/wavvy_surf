from django.shortcuts import render
from channel.models import Video
from commu.models import Post
from spot.models import ForcastData


def index(request):
    video_count= Video.objects.count()
    video_list = Video.objects.all()
    spot_list = ForcastData.objects.all()
    return render(request, 'allpage/index.html',{
        'usedMarket' : Post.objects.filter(category='1').order_by('-pub_date'), #중고장터
        'carpool' : Post.objects.filter(category='2').order_by('-pub_date'), #같이가요
        'meeting' : Post.objects.filter(category='4').order_by('-pub_date'), #정모/번개
        'information' : Post.objects.filter(category='3').order_by('-pub_date'), #강습정보
        'notice': Post.objects.filter(category='5').order_by('-pub_date'), #공지사항


        'video_list':video_list,
        'video_count':video_count,
        'spot_list':spot_list,
        })


def terms(request):
    return render(request, 'allpage/terms.html')


def privacy(request):
    return render(request, 'allpage/privacy.html')
