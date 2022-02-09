from dataclasses import fields
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Accessory
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', { 'guitars': guitars})

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    accessory_ids = guitar.accessories.all().values_list('id')
    accessories = Accessory.objects.exclude(id__in=accessory_ids)
    return render(request, 'guitars/detail.html', { 
        'guitar': guitar,
        'accessories': accessories
    })

# Class-Based Views

class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = '__all__'

class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/index.html'

class AccessoryList(ListView):
    model = Accessory

class AccessoryDetail(DetailView):
    model = Accessory

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = '__all__'

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'

def assoc_accessory(request, guitar_id, accessory_id):
    guitar = Guitar.objects.get(id=guitar_id)
    guitar.accessories.add(accessory_id)
    return redirect('detail', guitar_id=guitar_id)