from django.shortcuts import render
from django.db.models import F,Sum
from django.http import JsonResponse,HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from adminapp.models import Flight,FlightDetails,Reservation,Food,Beverages,Airport
from adminapp.serializers import FlightDetailsSerializer,FlightSerializer,FoodSerializer,BeveragesSerializer,ReservationSerializer
from adminapp.forms import SaveReservation
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json
from django.core.serializers import serialize
from datetime import timedelta


   
def set_if_not_none(mapping,key,value):
    if value is not None:
        mapping[key]=value

class FlightList(APIView):
        
    def get(self,request):
        flight_code = request.GET.get('flight_code')
        from_airport__city = request.GET.get('from_location')
        to_airport__city = request.GET.get('to_location')
        no_of_stops=request.GET.get('no_of_stops')
        duration_start=request.GET.get('duration_start')
        duration_stop=request.GET.get('duration_stop')
        if duration_start and duration_stop:
            duration_start=timedelta(hours=float(duration_start))
            duration_stop=timedelta(hours=float(duration_stop))
        else:
            duration_stop=None
            duration_start=None
        
        flight_params={}

        set_if_not_none(flight_params, 'flight_code', flight_code)
        set_if_not_none(flight_params, 'from_airport__city', from_airport__city)
        set_if_not_none(flight_params, 'to_airport__city', to_airport__city)
        set_if_not_none(flight_params, 'no_of_stops', no_of_stops)
        set_if_not_none(flight_params,'duration__range',(duration_start,duration_stop))
        try:
            flight_list = FlightDetails.objects.filter(**flight_params)
            if flight_list is None:
                return HttpResponse()
            serializer=FlightDetailsSerializer(flight_list,many=True)
            return Response(serializer.data)
        except:
            return HttpResponseNotFound("<h1>Enter valid parameters!</h1>")


class FlightDetail(APIView):
    def get_object(self,pk):
        try:
            return FlightDetails.objects.get(id=pk)
        except FlightDetails.DoesNotExist:
            raise HttpResponseNotFound("<h1>Flight does'nt exist!</h1>")

    def get(self,request,pk):
        flight=self.get_object(pk)
        serializer=FlightDetailsSerializer(flight)
        x=serializer.data
        firstclass_seats=FlightDetails.fc_seats(flight)
        business_seats=FlightDetails.bc_seats(flight)
        economy_seats=FlightDetails.ec_seats(flight)
        y={'firstclass_seats':firstclass_seats,
           'business_seats':business_seats,
           'economy_seats':economy_seats,}
        x.update(y)
        return Response(x)


class Reservations(APIView):
    
    def get_object(self,pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise HttpResponseNotFound("<h1>Reservation does'nt exist! or you may have entered it wrongly</h1>")
        
    def put(self,request,pk):
        reservation=self.get_object(pk)
        serializer=ReservationSerializer(reservation)
        return Response(serializer.data)


def total_price(flight,type,food,beverages):
    total=0
    x=flight
    if type=="1":
        total+=x.firstclass_price
    elif type=="2":
        total+=x.business_price
    elif type=="3":
        total+=x.economy_price
    
    if food.exists():
        t=food.values().aggregate(Sum('food_price'))
        total+=t['food_price__sum']
    else:
        total+=0
    
    if beverages.exists():
        t=beverages.values().aggregate(Sum('beverages_price'))
        total+=t['beverages_price__sum']
    else:
        total+=0
    return total
  
def save_reservation(request):
   
    if request.method=="POST":
        form=SaveReservation(request.POST)
        
        if form.is_valid():
           
           flight=form.cleaned_data['flight']
           type=form.cleaned_data['type']
           food=form.cleaned_data['food']
           beverages=form.cleaned_data['beverages']
           
           obj=form.save(commit=False)
           obj.price=total_price(flight,type,food)
           obj.status="1"
           obj.save()
           form.save_m2m()
                  
    else:
        form=SaveReservation()
    return render(request,"reservation.html",{
        'form':form,
    })

