from .models import Flight,FlightDetails,Reservation,Airport,Food,Beverages
from django import forms

class SaveReservation(forms.ModelForm):
    adults=forms.IntegerField(min_value=1)
    children=forms.IntegerField(min_value=0)
    infants=forms.IntegerField(min_value=0)

    class Meta:
        model=Reservation
        exclude=('status','price',)

    def clean(self):
        cleaned_data=super().clean()
        adults=cleaned_data.get('adults')
        children=cleaned_data.get('children')
        infants=cleaned_data.get('infants')
        total_tickets=adults+children+infants
        if total_tickets>9:
            raise forms.ValidationError("Maximum 9 tickets can be booked at a time.")
    
    """   
    def save(self,commit=True):
        instance=super().save(commit=False)
        instance.food.set(self.cleaned_data['food'])
        instance.beverages.set(self.cleaned_data['beverages'])
        if commit:
            instance.save()
        return instance
    """