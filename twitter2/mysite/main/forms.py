from django import forms
from .models import mode

class create(forms.ModelForm):
    class Meta:
        model = mode
        fields = '__all__'