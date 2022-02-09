from django.forms import ModelForm
from .models import Stringing

class StringingForm(ModelForm):
    class Meta:
        model = Stringing
        fields = ['date', 'brand', 'gauge']