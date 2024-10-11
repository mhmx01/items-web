from django.contrib.auth.mixins import LoginRequiredMixin
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


class ItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = Item
    fields = ("title", "content")
    template_name = "items/item_new.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
