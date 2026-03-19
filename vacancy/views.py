from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from . import forms


class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = forms.CustomRegisterForm
    success_url = reverse_lazy('login')


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('congratulation')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('login')


class CongratulationView(generic.ListView):
    template_name = 'cong.html'
    model = User
    context_object_name = 'user'