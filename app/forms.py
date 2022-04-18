from django import forms
from django.core.exceptions import ValidationError
from .models import CV 

class send_cv(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('name', 'email', 'image')
        labels = {'name':"Ваше ФИО", 'image':"Фото резюме", 'email':"Ваша электронная почта" } 
