from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,Http404
from adminapp.models import Flight,FlightDetails,PassengerProfile,TicketInfo
from adminapp.serializers import FlightSerializer,FlightDetailsSerializer,PassengerProfileSerializer,TicketInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q,Sum
from rest_framework.views import APIView
import json
from django.core.serializers import serialize
"""
def index(request):
    flights=Flight.objects.all()
    flight_detail=FlightDetails.objects.all()
    return render(request, "index.html",{
        "flights":flights,
        "flight_detail":flight_detail
    })
def total_seats(id):
    z=0
    x=TicketInfo.objects.filter(flight_id=id).aggregate(y=Sum('no_seats'))
    z=x["y"]
    if z==None:
        return 0
    return z
  
@api_view(['POST'])
def find_flights(request):
    flights=Flight.objects.filter(Q(airline_name=request.data['airline_name']) | Q(from_location=request.data['from_location']) | Q(to_location=request.data['to_location']))
    serializer=FlightSerializer(flights,many=True)
    return Response(serializer.data)

def find_flights(request):
    flights=Flight.objects.all()
    search_term=""
    if 'search' in request.GET:
        search_term=request.GET['search']
        flights=flights.filter(
            Q(airline_name__icontains=search_term)|
            Q(from_location__icontains=search_term)|
            Q(to_location__icontains=search_term)
        )
        context={
            'flights':flights,
            'search_term':search_term,
            
        }

@api_view(['GET'])
def view_flight(request,pk):
    flight=Flight.objects.get(pk=pk)
    flight_detail=FlightDetails.objects.get(pk=pk)
    m=total_seats(pk)

    availble_seats=flight_detail.available_seats-m
    return render(request, 'flight_detail.html',{
        "flight_id":flight.flight_id,
        "airline_name":flight.airline_name,
        "from_location":flight.from_location,
        "to_location":flight.to_location,
        "departure":flight.departure,
        "flight_departure_date":flight_detail.flight_departure_date,
        "price":flight_detail.price,
        "availble_seats":availble_seats
    })


@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(flight_id=request.data['flightId'])


    passenger=PassengerProfile()
    passenger.profile_id=request.data['profile_id']
    passenger.first_name=request.data['first_name']
    passenger.last_name=request.data['last_name']
    passenger.phone=request.data['phone']
    passenger.email=request.data['email']
    passenger.save()

    

    ticketInfo=TicketInfo()
    ticketInfo.profile_id=passenger
    ticketInfo.flight_id=flight
    ticketInfo.no_seats=request.data['no_seats']
    ticketInfo.save()
    return Response(status=status.HTTP_201_CREATED)
"""
   
def set_if_not_none(mapping,key,value):
    if value is not None:
        mapping[key]=value
class FlightList(APIView):
    def get(self,request):
        flight_id = request.GET.get('flight_id')
        from_location = request.GET.get('from_location')
        to_location = request.GET.get('to_location')
        
        flight_params={}

        set_if_not_none(flight_params, 'flight_id', flight_id)
        set_if_not_none(flight_params, 'from_location', from_location)
        set_if_not_none(flight_params, 'to_location', to_location)

        flight_list = Flight.objects.filter(**flight_params)
        serializer=FlightSerializer(flight_list,many=True)
        
        return Response(serializer.data)


class FlightDetail(APIView):
    def get_object(self,pk):
        try:
            return FlightDetails.objects.get(pk=pk)
        except Flight.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        flight=self.get_object(pk)
        serializer=FlightDetailsSerializer(flight)
        return Response(serializer.data)    
class ReservationList(APIView):
    def get(self,request):
        reservation=TicketInfo.objects.all()
        serialized_data=serialize("json",reservation)
        serialized_data=json.loads(serialized_data)
        return JsonResponse(serialized_data,safe=False,status=200)