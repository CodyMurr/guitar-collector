from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Guitar, Accessory
from .forms import StringingForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def guitars_index(request):
    guitars = Guitar.objects.filter(user=request.user)

    return render(request, 'guitars/index.html', { 'guitars': guitars})

@login_required
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

class GuitarCreate(LoginRequiredMixin, CreateView):
    model = Guitar
    fields = ['brand', 'model', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GuitarUpdate(LoginRequiredMixin, UpdateView):
    model = Guitar
    fields = ['brand', 'model', 'description']


class GuitarDelete(LoginRequiredMixin, DeleteView):
    model = Guitar
    success_url = '/guitars/'

@login_required
def add_stringing(request, guitar_id):
    form = StringingForm(request.POST)
    if form.is_valid():
        new_stringing = form.save(commit=False)
        new_stringing.guitar_id = guitar_id
        new_stringing.save()
    return redirect('detail', guitar_id=guitar_id)

class AccessoryList(LoginRequiredMixin, ListView):
    model = Accessory

class AccessoryDetail(LoginRequiredMixin, DetailView):
    model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    fields = ['brand', 'name', 'accessory_type']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
    model = Accessory
    success_url = '/accessories/'

@login_required
def assoc_accessory(request, guitar_id, accessory_id):
    guitar = Guitar.objects.get(id=guitar_id)
    guitar.accessories.add(accessory_id)
    return redirect('detail', guitar_id=guitar_id)

@login_required
def unassoc_accessory(request, guitar_id, accessory_id):
    guitar = Guitar.objects.get(id=guitar_id)
    guitar.accessories.remove(accessory_id)
    return redirect('detail', guitar_id=guitar_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign Up - Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)