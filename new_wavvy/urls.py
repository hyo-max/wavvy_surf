"""new_wavvy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views  # import this
from django.urls import path, include

import allpage.views

urlpatterns = [
    path('', allpage.views.index, name='index'),
    path('policy/', include('allpage.urls')),
    path('account/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('channel/', include('channel.urls')),
    path('commu/', include('commu.urls')),
    path('spot/', include('spot.urls')),
    path('school/', include('school.urls')),
    path('iamport/', include('iamport.urls', namespace='iamport')),

    path('i18n/', include('django.conf.urls.i18n')),

    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_complete'),
]

urlpatterns += i18n_patterns(
    path('shop/', include(apps.get_app_config('oscar').urls[0]))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
