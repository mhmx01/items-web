import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def generate_unique_slug(value):
    """generate unique slug using uuid4 that build on a base value."""
    return "{}-{}".format(slugify(value), str(uuid.uuid4()).split("-")[0])


class Item(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="items"
    )

    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="items_liked", blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("item_detail", args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["-created_at"])]
