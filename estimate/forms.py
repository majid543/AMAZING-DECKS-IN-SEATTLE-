from django import forms
from .models import UserInput

class UserInputForm(forms.ModelForm):
    age = forms.IntegerField(
        label='Age',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
    )
    distance = forms.DecimalField(
        label='Distance',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the distance'}),
    )
    deck_height = forms.DecimalField(
        label='Deck Height',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the deck height'}),
    )

    class Meta:
        model = UserInput
        fields = ['age', 'distance', 'deck_height']


class ScheduleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'name': 'Name', 'placeholder': 'Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'name': 'Email', 'placeholder': 'Email'})
    )