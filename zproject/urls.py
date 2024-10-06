import environ
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

env = environ.Env()


urlpatterns = [
    path(env.str("ADMIN_URL"), admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
