from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("follow/", views.user_follow, name="user_follow"),
    path("<username>/", views.user_detail, name="user_detail"),
]
