from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Item


class ItemsAppTestCase(TestCase):
    item_fields = {
        "title": "item #1 title",
        "content": "item #1 content",
    }
    user_fields = {
        "username": "first_user",
        "password": "super_secret",
    }

    def setUp(self):
        self.user = get_user_model().objects.create_user(**self.user_fields)
        self.item_fields["owner"] = self.user
        self.item = Item.objects.create(**self.item_fields)


class ItemModelTests(ItemsAppTestCase):
    def test_fields(self):
        self.assertEqual(self.item.title, self.item_fields["title"])
        self.assertEqual(self.item.content, self.item_fields["content"])
        self.assertTrue(hasattr(self.item, "created_at"))
        self.assertTrue(hasattr(self.item, "updated_at"))

    def test_relationships(self):
        self.assertEqual(self.item.owner, self.user)
        self.assertEqual(self.user.items.first(), self.item)

    def test_methods(self):
        self.assertEqual(str(self.item), self.item.title)
        self.assertEqual(self.item.get_absolute_url(), f"/items/{self.item.pk}/")

    def test_ordering(self):
        """should list most recent items first."""
        second_item_fields = {
            "title": "item #2 title",
            "content": "item #2 content",
            "owner": self.user,
        }
        second_item = Item.objects.create(**second_item_fields)
        self.assertEqual(Item.objects.first(), second_item)


class ItemListViewTests(ItemsAppTestCase):
    def test_get(self):
        response = self.client.get("/items/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "items/item_list.html")
        self.assertContains(
            response, f'<a href="{self.item.get_absolute_url()}">{self.item}</a>'
        )


class ItemDetailViewTests(ItemsAppTestCase):
    def test_get(self):
        response = self.client.get("/items/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "items/item_detail.html")
        self.assertContains(response, f"<h2>Item: {self.item}</h2>")
