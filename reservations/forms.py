# forms.py
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'guests']

    widgets = {
        'time': forms.TimeInput(format='%H:%M'),
    }
