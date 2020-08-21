from django.db import models
from restaurant.models import Information


class PlateType(models.Model):
    restaurant = models.ForeignKey(
        Information,
        on_delete=models.CASCADE,
        default=None,
    )
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return str(self.name)


class Plate(models.Model):
    restaurant = models.ForeignKey(
        Information,
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
    plate_type = models.ManyToManyField(
        PlateType,
    )
    price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        default=0.00,
    )

    def __str__(self):
        return str(self.name)
