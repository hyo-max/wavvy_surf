from django.shortcuts import render,redirect
from channel.models import Video
from commu.models import Post
from school.models import Post as SchoolPost
from spot.models import ForcastData

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


def index(request):
    video_count= Video.objects.count()
    video_list = Video.objects.all()
    school_list = SchoolPost.objects.all()
    spot_list = ForcastData.objects.all()
    return render(request, 'allpage/index.html',{
        'usedMarket' : Post.objects.filter(category='1').order_by('-pub_date'), #중고장터
        'carpool' : Post.objects.filter(category='2').order_by('-pub_date'), #같이가요
        'meeting' : Post.objects.filter(category='3').order_by('-pub_date'), #정모/번개
        'information' : Post.objects.filter(category='4').order_by('-pub_date'), #강습정보
        'notice': Post.objects.filter(category='5').order_by('-pub_date'), #공지사항

        'school_list':school_list,
        'video_list':video_list,
        'video_count':video_count,
        'spot_list':spot_list,
        })

def terms(request):
    return render(request, 'allpage/terms.html')


def privacy(request):
    return render(request, 'allpage/privacy.html')

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            
            return redirect('success')
    return render(request, "allpage/email.html", {'form': form})

def successView(request):
    return render(request, "allpage/success.html")


'''
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['wavvy.surf@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "allpage/email.html", {'form': form})

def successView(request):
    return render(request, "allpage/success.html")

'''