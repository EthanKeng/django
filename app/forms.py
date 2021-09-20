from django import forms
from .models import Card


class AddCard(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['first_name', 'last_name', 'company',
                   'title', 'sideBusiness', 'email', 'country', 'city']
