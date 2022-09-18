from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
