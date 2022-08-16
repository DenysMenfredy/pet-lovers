from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from pathlib import Path
# Create your views here.
from .models import LoginForm

class UserLogin(LoginView):
    model = LoginForm
    template_name:str = 'login/login.html'
    def get(self, request):
        print(Path.cwd())
        return render(request, self.template_name)

    def post(self, request):
        return HttpResponse('Login')
