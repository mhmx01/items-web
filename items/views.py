from django.views import generic

from .models import Item


class ItemListView(generic.ListView):
    model = Item
    template_name = "items/item_list.html"
    context_object_name = "items"


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = "items/item_detail.html"
    context_object_name = "item"
