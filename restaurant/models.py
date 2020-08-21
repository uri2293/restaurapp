from django.db import models
from django.contrib.auth.models import User


class Information(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=30,
    )
    description = models.TextField(
        max_length=300,
    )
    image = models.ImageField(
        upload_to='uploads',
        blank=True,
    )
    phone = models.CharField(
        max_length=12,
    )

    def __str__(self):
        return str(self.name)
