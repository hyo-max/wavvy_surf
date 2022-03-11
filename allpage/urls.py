from django.urls import path
from . import views

urlpatterns = [
    path('terms/',views.terms, name='terms'),
    path('privacy/',views.privacy, name='privacy'),

    path('contact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),
    ]