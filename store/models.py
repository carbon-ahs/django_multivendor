from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Catagory(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"))

    class Meta:
        verbose_name = "Catagory"
        verbose_name_plural = "Catagories"

    def __str__(self):
        return self.title


class Product(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        related_name="products",
        on_delete=models.CASCADE,
    )
    catagory = models.ForeignKey(
        Catagory,
        verbose_name=_("Catagory"),
        related_name="products",
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"))
    description = models.TextField(
        _("Description"),
        blank=True,
    )
    price = models.IntegerField(_("Price"))
    created_at = models.DateTimeField(
        _("Created At"),
        auto_now=False,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
        auto_now_add=False,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price
