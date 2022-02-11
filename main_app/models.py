from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

GAUGES = (
    ('E', 'Extra-Light'),
    ('L', 'Light'),
    ('M', 'Medium'),
    ('H', 'Heavy')
)

class Accessory(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    accessory_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})

class Guitar(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})


class Stringing(models.Model):
    date = models.DateField()
    brand = models.CharField(max_length=50)
    gauge = models.CharField(
        max_length=1,
        choices=GAUGES,
        default=GAUGES[1][0]
    )
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Changed to {self.get_gauge_display()} {self.brand} on {self.date}"