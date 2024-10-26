from django.urls import path

from . import views

urlpatterns = [
    path("new/", views.ItemCreateView.as_view(), name="item_new"),
    path("", views.ItemListView.as_view(), name="item_list"),
    path("<slug:slug>/", views.ItemDetailView.as_view(), name="item_detail"),
    path("<slug:slug>/delete/", views.ItemDeleteView.as_view(), name="item_delete"),
    path("<slug:slug>/edit/", views.ItemUpdateView.as_view(), name="item_edit"),
]
