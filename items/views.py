from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import ItemShareForm
from .models import Item


class ItemListView(generic.ListView):
    model = Item
    template_name = "items/item_list.html"
    context_object_name = "items"
    paginate_by = 10


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


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Item
    fields = ("title", "content")
    template_name = "items/item_edit.html"

    def test_func(self):
        return self.request.user == self.get_object().owner


def item_share(request, slug):
    item = get_object_or_404(Item, slug=slug)
    sent = False
    if request.method == "POST":
        form = ItemShareForm(request.POST)
        if form.is_valid():
            item_url = request.build_absolute_uri(item.get_absolute_url())
            cd = form.cleaned_data
            message = (
                f"{cd['name']} ({cd['email']}) recommend you read: ({item.title}) at {item_url}\n"
                + (
                    f"\n------\n{cd['name']} comments:\n“{cd['comments']}”"
                    if cd["comments"]
                    else ""
                )
            )
            send_mail(
                subject=f"Recommended Item from {cd['name']}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[cd["to"]],
                fail_silently=False,
            )
            sent = True
    else:
        form = ItemShareForm()
    return render(
        request, "items/item_share.html", {"form": form, "item": item, "sent": sent}
    )
