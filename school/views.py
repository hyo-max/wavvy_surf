from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    )

from .models import Post
from new_wavvy.settings import GOOGLE_MAPS_API_KEY


def school_list(request):
    school_list = Post.objects.all()
    east = Post.objects.filter(category='1').order_by('title') #동해안
    south = Post.objects.filter(category='2').order_by('title') #남해안
    west = Post.objects.filter(category='3').order_by('title') #서해안
    jeju = Post.objects.filter(category='4').order_by('title') #제주
    

    return render(request, 'school/school_list.html',{
        'school_list':school_list,
        'east':east,
        'south':south,
        'west':west,
        'jeju':jeju,
        })


class SchoolListView(ListView):
    model = Post
    template_name = 'school/school_list.html'  # <app>/<model>_<viewtype>.html   
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 20
    

class SchoolDetailView(DetailView):
    model = Post
    template_name = 'school/school_detail.html' 

    def get_context_data(self, **kwargs):
        context = super(SchoolDetailView, self).get_context_data(**kwargs)
        context["maps"]  = 'AIzaSyA2fz26mU9R96fsaCBAxEcYwjWOPxl6kJY'
        return context

