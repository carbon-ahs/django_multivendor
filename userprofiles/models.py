from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("User Profile"),
        related_name="userprofile",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username
