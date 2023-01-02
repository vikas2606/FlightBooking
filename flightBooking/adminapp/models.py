from django.db import models


# Create your models here.
class Flight(models.Model):
    flight_id=models.IntegerField(primary_key=True)
    airline_name=models.CharField(max_length=20)
    from_location=models.CharField(max_length=20)
    to_location=models.CharField(max_length=20)
    departure=models.TimeField()
    arrival=models.TimeField()
    total_seats=models.IntegerField()

    """
    def __str__(self):
        return str(self.flight_id)+self.airline_name
    """

class FlightDetails(models.Model):
    flight_id=models.ManyToManyField(Flight)
    flight_departure_date=models.DateField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    available_seats=models.IntegerField()

class PassengerProfile(models.Model):
    profile_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return str(self.profile_id)+" "+self.last_name

class TicketInfo(models.Model):
    ticket_id=models.IntegerField(primary_key=True)
    profile_id=models.ForeignKey(PassengerProfile, on_delete=models.CASCADE)
    flight_id=models.ForeignKey(Flight, on_delete=models.CASCADE)
    no_seats=models.IntegerField(default=1)

