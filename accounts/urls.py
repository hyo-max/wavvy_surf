from django.contrib.auth.views import LogoutView
from django.urls import path


from . import views

urlpatterns = [
    #path('create/', UserRegistrationView.as_view(), name='create'),    # 회원가입
    #path('login/', UserLoginView.as_view(), name='login'),         # 로그인
    #path('logout/', LogoutView.as_view(), name='logout'),       #로그아웃
    path('profile/',views.profile, name='profile'),       #마이페이지

]


