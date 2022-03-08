from django.shortcuts import render, get_object_or_404
from .models import Video
from django.core.paginator import Paginator


def channel_list(request):
    videos = Video.objects
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'channel/channel_list.html',{
        'videos' : videos,
        'video_list':video_list,
        'posts':posts
        })

def channel_detail(request, video_id):
    video_detail = get_object_or_404(Video,pk=video_id)
    return render(request, 'channel/channel_detail.html',{'video_detail':video_detail})

