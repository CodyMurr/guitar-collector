from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Accessory
from .forms import StringingForm
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
    stringing_form = StringingForm()
    accessory_ids = guitar.accessories.all().values_list('id')
    accessories = Accessory.objects.exclude(id__in=accessory_ids)
    return render(request, 'guitars/detail.html', { 
        'guitar': guitar,
        'stringing_form': stringing_form,
        'accessories': accessories
    })

# Class-Based Views

class GuitarCreate(CreateView):
    model = Guitar
    fields = ['brand', 'model', 'description']

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ['brand', 'model', 'description']

class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/'

def add_stringing(request, guitar_id):
    form = StringingForm(request.POST)
    if form.is_valid():
        new_stringing = form.save(commit=False)
        new_stringing.guitar_id = guitar_id
        new_stringing.save()
    return redirect('detail', guitar_id=guitar_id)

class AccessoryList(ListView):
    model = Accessory

class AccessoryDetail(DetailView):
    model = Accessory

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['brand', 'name', 'accessory_type']

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'

def assoc_accessory(request, guitar_id, accessory_id):
    guitar = Guitar.objects.get(id=guitar_id)
    guitar.accessories.add(accessory_id)
    return redirect('detail', guitar_id=guitar_id)

def unassoc_accessory(request, guitar_id, accessory_id):
    guitar = Guitar.objects.get(id=guitar_id)
    guitar.accessories.remove(accessory_id)
    return redirect('detail', guitar_id=guitar_id)