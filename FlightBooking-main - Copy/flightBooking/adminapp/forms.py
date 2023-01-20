from .models import Flight,FlightDetails,Reservation,Airport,Food,Beverages
from django import forms

class SaveReservation(forms.ModelForm):
    class Meta:
        model=Reservation
        fields="__all__"

class SaveFood(forms.ModelForm):
    class Meta:
        model=Food
        fields="__all__"