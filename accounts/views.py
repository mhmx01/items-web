import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
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


@require_POST
@login_required
def user_follow(request):
    payload = json.loads(request.body)
    action = payload.get("action")
    username = payload.get("username")
    if action not in ("follow", "unfollow"):
        return JsonResponse({"status": "error"})
    user = get_object_or_404(CustomUser, username=username)
    if action == "follow":
        user.followers.add(request.user)
    elif action == "unfollow":
        user.followers.remove(request.user)
    return JsonResponse({"status": "ok"})
