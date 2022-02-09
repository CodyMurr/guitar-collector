from django.db import models
from django.urls import reverse

# Create your models here.

class Accessory(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    accessory_type = models.CharField(max_length=50)

class Guitar(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})