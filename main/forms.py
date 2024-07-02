from django import forms
from .models import task


class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'important']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'important': 'Importante',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
 