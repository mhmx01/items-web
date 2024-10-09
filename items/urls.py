from django.urls import path

from . import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name="item_list"),
    path("<int:pk>/", views.ItemDetailView.as_view(), name="item_detail"),
]
