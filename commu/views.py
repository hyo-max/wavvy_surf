from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
    )
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


from .models import Post,Category,Comment

def commu_list(request):
    usedMarket = Post.objects.filter(category='1').order_by('-pub_date') #중고장터
    carpool = Post.objects.filter(category='2').order_by('-pub_date') #같이가요
    meeting = Post.objects.filter(category='4').order_by('-pub_date') #정모/번개
    information = Post.objects.filter(category='3').order_by('-pub_date') #강습정보
    notice = Post.objects.filter(category=5).order_by('-pub_date') #공지사항

    usedMarket_paginator = Paginator(usedMarket, 30)
    usedMarket_page = request.GET.get('page')
    usedMarket_posts = usedMarket_paginator.get_page(usedMarket_page)

    carpool_paginator = Paginator(carpool, 30)
    carpool_page = request.GET.get('page')
    carpool_posts = carpool_paginator.get_page(carpool_page)

    paginator = Paginator(meeting, 30)
    page = request.GET.get('page')
    meeting_posts = paginator.get_page(page)

    paginator = Paginator(information, 30)
    page = request.GET.get('page')
    information_posts = paginator.get_page(page)

    return render(request, 'commu/commu_list.html',{
        'usedMarket' : usedMarket,
        'carpool' : carpool,
        'meeting' : meeting,
        'information' : information,
        'usedMarket_posts': usedMarket_posts,
        'carpool_posts': carpool_posts,
        'meeting_posts': meeting_posts,
        'information_posts': information_posts,
        'notice':notice,
    })

class PostListView(ListView):
    model = Post
    template_name = 'commu/commu_list.html'  # <app>/<model>_<viewtype>.html   
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 8
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'commu/commu_detail.html' 

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['category','title', 'body']
    template_name = 'commu/commu_form.html' 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['category','title', 'body']
    template_name = 'commu/commu_form.html' 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'commu/commu_confirm_delete.html' 
    success_url = '/commu/commu_list/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def newreply(request):
        if request.method == 'POST':
                comment = Comment()
                comment.comment_body = request.POST['comment_body']
                comment.blog = Post.objects.get(pk=request.POST['blog']) # id로 객체 가져오기        
                comment.comment_user = request.user
                comment.save()
                return redirect('/commu/commu_detail/'+ str(comment.blog.id))
        else :
                return redirect('index') # 홈으로

