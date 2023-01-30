from rest_framework import serializers
from .models import Flight,FlightDetails,Airport,Reservation,Food,Beverages

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Airport
        fields='__all__'

class FlightDetailsSerializer(serializers.ModelSerializer):
    #from_airport=AirportSerializer()
    class Meta:
        model=FlightDetails
        fields='__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields='__all__'

class BeveragesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Beverages
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'