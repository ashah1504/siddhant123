from django import forms
from .models import course

class courseForms(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'