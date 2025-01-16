from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


def user_detail(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, "accounts/user_detail.html", {"this_user": user})
