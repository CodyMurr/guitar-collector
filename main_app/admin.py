from django.contrib import admin
from .models import Accessory, Guitar, Stringing

# Register your models here.

admin.site.register(Guitar)
admin.site.register(Accessory)
admin.site.register(Stringing)