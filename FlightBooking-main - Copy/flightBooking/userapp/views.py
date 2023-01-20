from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from adminapp.models import Flight,FlightDetails,Reservation,Food,Beverages,Airport
from adminapp.serializers import FlightDetailsSerializer,FlightSerializer,FoodSerializer,BeveragesSerializer,ReservationSerializer
from adminapp.forms import SaveReservation,SaveFood
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json
from django.core.serializers import serialize


   
def set_if_not_none(mapping,key,value):
    if value is not None:
        mapping[key]=value

class FlightList(APIView):
        
    def get(self,request):
        flight_code = request.GET.get('flight_code')
        from_airport__city = request.GET.get('from_location')
        to_airport__city = request.GET.get('to_location')
        no_of_stops=request.GET.get('no_of_stops')
        
        flight_params={}

        set_if_not_none(flight_params, 'flight_code', flight_code)
        set_if_not_none(flight_params, 'from_airport__city', from_airport__city)
        set_if_not_none(flight_params, 'to_airport__city', to_airport__city)
        set_if_not_none(flight_params, 'no_of_stops', no_of_stops)
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
            return FlightDetails.objects.get(flight_name__flight_id=pk)
        except FlightDetails.DoesNotExist:
            raise HttpResponseNotFound("Flight does'nt exist!")

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
"""
class Reservation(APIView):
    
    
    def post(self,request):
        form=SaveReservation(request.POST)
        if form.is_valid():
            flight=form.cleaned_data['flight']
            type=form.cleaned_data['type']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            gender=form.cleaned_data['gender']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            address=form.cleaned_data['address']
            food=form.cleaned_data['food']
            beverages=form.cleaned_data['beverages']

            reservation=Reservation(flight=flight,type=type,first_name=first_name,last_name=last_name,gender=gender,email=email,mobile=mobile,address=address,food=food,beverages=beverages,status="successful")

            
            reservation=Reservation(
            
            flight=form.cleaned_data['flight'],
            type=form.cleaned_data['type'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            gender=form.cleaned_data['gender'],
            email=form.cleaned_data['email'],
            mobile=form.cleaned_data['mobile'],
            address=form.cleaned_data['address'],
            food=form.cleaned_data['food'],
            beverages=form.cleaned_data['beverages'],

            )
            
        
            

            reservation.save()
            return HttpResponse("<h1>thank</h1>")
        
        form=SaveReservation()

        return render(request, "reservation.html",{
            "form":form



        })
  """      

def save_reservation(request):
    if request.method=="POST":
        form=SaveReservation(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form=SaveReservation()
    return render(request,"reservation.html",{
        'form':form
    })
"""

def save_reservation(request):
    flight=FlightDetails.objects.get(id=request.data['flightid'])

    food=Food()
    food.food_id=request.data['food_id']
    food.food_name=request.data['food_item']
    food.food_price=request.data['food_price']
    food.save()

    beverages=Beverages()
    beverages.beverages_id=request.data['beverages_id']
    beverages.beverages_name=request.data['beverages_item']
    beverages.beverages_price=request.data['beverages_price']
    beverages.save()

    reservation=Reservation()
    reservation.flight=flight
    reservation.type=request.data['type']
    reservation.first_name=request.data['first_name']
    reservation.last_name=request.data['last_name']
    reservation.gender=request.data['gender']
    reservation.email=request.data['email']
    reservation.mobile=request.data['mobile']
    reservation.address=request.data['address']
    reservation.food=food
    reservation.beverages=beverages
    reservation.status="Successful"
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)

"""
