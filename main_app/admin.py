from django.contrib import admin
from .models import Accessory, Stringing, Guitar 

# Register your models here.

admin.site.register(Guitar)
admin.site.register(Stringing)
admin.site.register(Accessory)