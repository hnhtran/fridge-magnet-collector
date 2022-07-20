from django.forms import ModelForm
from .models import Surface

class SurfaceForm(ModelForm):
    class Meta:
        model = Surface
        fields = ['date', 'where']