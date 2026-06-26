from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'special_requests']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': '+977 9XX-XXXXXXX', 'class': 'form-input'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            'guests': forms.NumberInput(attrs={'min': 1, 'max': 50, 'class': 'form-input'}),
            'special_requests': forms.Textarea(attrs={'placeholder': 'Any special requests or notes...', 'rows': 4, 'class': 'form-input'}),
        }
