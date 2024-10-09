from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at", "updated_at")
    list_filter = ("owner", "created_at", "updated_at")
    search_fields = ("title", "content")

    readonly_fields = ("created_at", "updated_at")
    raw_id_fields = ("owner",)
