from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Booking
        fields = '__all__'
