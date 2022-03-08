from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
    )

urlpatterns = [
    path('commu_list/',views.commu_list, name='commu_list'),
    path('commu_list/',PostListView.as_view(), name='commu_list'),
    path('commu_detail/<int:pk>',PostDetailView.as_view(), name='commu-detail'),
    path('commu_detail/new',PostCreateView.as_view(),name='commu-create'),
    path('commu_detail/<int:pk>/update',PostUpdateView.as_view(),name='commu-update'),
    path('commu_detail/<int:pk>/delete',PostDeleteView.as_view(),name='commu-delete'),
    path('commu_detail/newreply',views.newreply, name="newreply"),
]
