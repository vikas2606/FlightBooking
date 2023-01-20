from django.shortcuts import render
from .models import Flight,FlightDetails,Airport,Food,Beverages,Reservation
from .serializers import FlightSerializer,FlightDetailsSerializer,AirportSerializer,ReservationSerializer,FoodSerializer,BeveragesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets,status

class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer

class FlightDetailsViewSet(viewsets.ModelViewSet):
    queryset=FlightDetails.objects.all()
    serializer_class=FlightDetailsSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

class AirportViewSet(viewsets.ModelViewSet):
    queryset=Airport.objects.all()
    serializer_class=AirportSerializer

class BeveragesViewSet(viewsets.ModelViewSet):
    queryset=Beverages.objects.all()
    serializer_class=BeveragesSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer


# Create your views here.
