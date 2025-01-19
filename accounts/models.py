from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        through="Friendship",
        related_name="followers",
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("user_detail", args=[self.username])


class Friendship(models.Model):
    from_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="friendship_from_me"
    )
    to_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="friendship_to_me"
    )
    since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Friendship(from: {self.from_user}, to: {self.to_user})"

    class Meta:
        unique_together = ["from_user", "to_user"]
