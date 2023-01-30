from django.db import models
from django.db.models.signals import post_save
from django.db.models import F,Sum
from django.utils import timezone
from django.dispatch import receiver
from django.utils.functional import cached_property


class Flight(models.Model):
    flight_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    status=models.CharField(max_length=2,choices=(('1','Active'),('2','Inactive')),default=1)
    date_added=models.DateTimeField(default=timezone.now)
    date_created=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="List of Flights"
    
    def __str__(self):
        return str(f"{self.name}")

class Airport(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    code=models.CharField(max_length=10)
    country=models.CharField(max_length=20)

    class Meta:
        verbose_name_plural="List of Airports"
    
    def __str__(self):
        return str(f"{self.name}")

class FlightDetails(models.Model):
    id=models.IntegerField(primary_key=True)
    flight_code=models.CharField(max_length=50)
    flight_name=models.ForeignKey(Flight, on_delete=models.CASCADE)
    from_airport=models.ForeignKey(Airport, on_delete=models.CASCADE,related_name="From_Airport")
    to_airport=models.ForeignKey(Airport, on_delete=models.CASCADE,related_name="To_Airport")
    departure=models.DateTimeField()
    arrival=models.DateTimeField()
    duration=models.DurationField()
    stops=models.ManyToManyField(Airport,null=True,blank=True)
    no_of_stops=models.IntegerField(default=0)
    economy_seats=models.IntegerField(default=0)
    business_seats=models.IntegerField(default=0)
    firstclass_seats=models.IntegerField(default=0)
    economy_price=models.FloatField(default=0)
    business_price=models.FloatField(default=0)
    firstclass_price=models.FloatField(default=0)
    date_created=models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{} {} {} {}".format(self.flight_code,self.flight_name.name,self.from_airport.city,self.to_airport.city)
    
    @cached_property
    def no_of_stops_count(self):
        return self.stops.all().count()
    
    def save(self,*args, **kwargs):
        self.no_of_stops=self.no_of_stops_count
        self.duration=self.arrival-self.departure
        super(FlightDetails,self).save(*args,**kwargs)

    def fc_seats(self):
        try:
            r=Reservation.objects.exclude(status=2).filter(flight=self,type=1).aggregate(total=Sum(F('adults')+F('children')+F('infants'))) 
            reservation=r['total']
            if reservation is None:
                reservation=0
        except:
            reservation=0

        return self.firstclass_seats-reservation
    
    def bc_seats(self):
        try:
            r=Reservation.objects.exclude(status=2).filter(flight=self,type=2).aggregate(total=Sum(F('adults')+F('children')+F('infants'))) 
            reservation=r['total']
            if reservation is None:
                reservation=0
        except:
            reservation=0

        return self.business_seats-reservation
        

    def ec_seats(self):
        try:
            r=Reservation.objects.exclude(status=2).filter(flight=self,type=3).aggregate(total=Sum(F('adults')+F('children')+F('infants'))) 
            reservation=r['total']
            if reservation is None:
                reservation=0
        except:
            reservation=0

        return self.economy_seats-reservation
    
    def save(self,*args, **kwargs):
        self.no_of_stops=self.no_of_stops_count
        self.duration=self.arrival-self.departure
        super(FlightDetails,self).save(*args,**kwargs)
    


class Food(models.Model):
    food_id=models.IntegerField(primary_key=1)
    food_name=models.CharField(max_length=50)
    food_price=models.IntegerField()

    def __str__(self):
        return "{} {} {}/-".format(self.food_id,self.food_name,self.food_price)
    


class Beverages(models.Model):       
    beverages_id=models.IntegerField(primary_key=1)
    beverages_name=models.CharField(max_length=50)
    beverages_price=models.IntegerField()

    def __str__(self):
        return "{} {} {}/-".format(self.beverages_id,self.beverages_name,self.beverages_price)


class Reservation(models.Model):
    flight=models.ForeignKey(FlightDetails, on_delete=models.CASCADE)
    type=models.CharField(max_length=50,choices=(('1','First Class'),('2','Business Class'),('3','Economy Class')),default=3)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female')),default='Male')
    adults=models.IntegerField(default=1)
    children=models.IntegerField(default=0)
    infants=models.IntegerField(default=0)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.TextField()
    food=models.ManyToManyField(Food,null=True,blank=True)
    beverages=models.ManyToManyField(Beverages,null=True,blank=True)
    status=models.CharField(max_length=50,choices=(('1','Successful'),('2','Cancelled')),default=2)
    date_created=models.DateTimeField(auto_now=True)   

    price=models.IntegerField(default=0) 

    class Meta:
        verbose_name_plural="List of Reservations"

    def __str__(self):
        return "{} {} {}".format(self.flight.flight_code,self.first_name,self.last_name)
    
    
    


