from django.urls import path
from . import views
from .views import SchoolDetailView, SchoolListView

urlpatterns = [
    path('school_list/',views.school_list, name='school_list'),
    path('school_list/',SchoolListView.as_view(), name='school_list'),
    path('school_detail/<int:pk>',SchoolDetailView.as_view(), name='school-detail'),
    
    ]