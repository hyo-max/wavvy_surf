from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm

from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy

from .models import User
from .forms import UserUpadateForm

'''
class UserRegistrationView(CreateView):     # 회원가입
    model = get_user_model()                # 자동생성 폼에서 사용할 모델
    form_class = UserRegistrationForm       # 자동생성 폼에서 사용할 필드
    success_url = '/account/login/'

class UserLoginView(LoginView):           # 로그인
    authentication_form = LoginForm
    template_name = 'accounts/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)    
'''

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpadateForm(request.POST,  request.FILES, instance=request.user)

        if u_form.is_valid() :
            u_form.save() 
            messages.success(request,f'your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpadateForm(instance=request.user)
    context = {
    'u_form' : u_form,
        }

    return render(request,'account/profile.html', context)

'''
   u_form = UserUpadateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpadateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'u_form' : u_form,
    'p_form' : p_form
    }
'''