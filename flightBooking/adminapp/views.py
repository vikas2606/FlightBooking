from django.shortcuts import render
from .models import PassengerProfile,Flight,FlightDetails,TicketInfo
from .serializers import PassengerProfileSerializer,FlightDetailsSerializer,FlightSerializer,TicketInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets,status

class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer

class FlightDetailsViewSet(viewsets.ModelViewSet):
    queryset=FlightDetails.objects.all()
    serializer_class=FlightDetailsSerializer

class PassengerProfileViewSet(viewsets.ModelViewSet):
    queryset=PassengerProfile.objects.all()
    serializer_class=PassengerProfileSerializer

class TicketInfoViewSet(viewsets.ModelViewSet):
    queryset=TicketInfo.objects.all()
    serializer_class=TicketInfoSerializer


# Create your views here.
