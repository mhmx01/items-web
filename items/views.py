from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
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


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Item
    template_name = "items/item_delete.html"
    success_url = reverse_lazy("item_list")

    def test_func(self):
        return self.request.user == self.get_object().owner
