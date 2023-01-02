from rest_framework import serializers
from .models import PassengerProfile,Flight,FlightDetails,TicketInfo

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'

class PassengerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=PassengerProfile
        fields='__all__'

class FlightDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlightDetails
        fields='__all__'

class TicketInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TicketInfo
        fields='__all__'
    
    def validate_no_seats(self,no_seats):
        if(no_seats>5):
            raise serializers.ValidationError("limit exceeded")
        return no_seats