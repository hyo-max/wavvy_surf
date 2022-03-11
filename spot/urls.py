from django.urls import path
from . import views
from .views import  SpotListView,SchoolDetailView

urlpatterns = [
    path('spot_list/',views.spot_list, name='spot_list'),
    path('spot_list/',SpotListView.as_view(), name='spot_list'),
    path('spot_detail/<int:pk>',SchoolDetailView.as_view(), name='spot_detail'),
    
    ]