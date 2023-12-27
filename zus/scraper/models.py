from django.db import models


class CoffeeShop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=25, null=True, blank=True)
    longitude = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.pk} | {self.name}"
