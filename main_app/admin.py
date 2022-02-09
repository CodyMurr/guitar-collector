from django.contrib import admin
from .models import Accessory, Guitar

# Register your models here.

admin.site.register(Guitar)
admin.site.register(Accessory)