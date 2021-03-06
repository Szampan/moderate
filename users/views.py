from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AuthorCreationForm


class SignUpView(CreateView):
    form_class = AuthorCreationForm
    success_url = reverse_lazy("users:login")
    template_name = "registration/signup.html"
