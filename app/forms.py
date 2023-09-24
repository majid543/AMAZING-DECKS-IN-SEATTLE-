from django import forms
from .models import Customers
import datetime


class CustomersForm(forms.ModelForm):
    Select_Date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control form-field', 'type': 'date'}))
    Select_Time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control form-field', 'type': 'time'}), required=False)
    class Meta:
        model = Customers
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-field'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-field'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-field'}),
        }
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Calculate tomorrow's date
        tomorrow = datetime.date.today() 

        # Set the 'min' attribute for the input field
        self.fields['Select_Date'].widget.attrs['min'] = tomorrow

class ScheduleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'name': 'Name', 'placeholder': 'Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'name': 'Email', 'placeholder': 'Email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'message', 'rows': '4', 'placeholder': 'Message', 'required': True})
    )