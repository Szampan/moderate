from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# import logout
from django.contrib.auth.views import LogoutView



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("users:login")
    template_name = "registration/signup.html"

    # Add additional info (first_name, last_name, etc.) to the user
