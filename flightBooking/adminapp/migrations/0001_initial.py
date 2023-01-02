# Generated by Django 4.1.3 on 2022-12-13 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.IntegerField(primary_key=True, serialize=False)),
                ('airline_name', models.CharField(max_length=20)),
                ('from_location', models.CharField(max_length=20)),
                ('to_location', models.CharField(max_length=20)),
                ('departure', models.TimeField()),
                ('arrival', models.TimeField()),
                ('total_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PassengerProfile',
            fields=[
                ('profile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TicketInfo',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False)),
                ('no_seats', models.IntegerField(default=0)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.flight')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.passengerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='FlightDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_departure_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('available_seats', models.IntegerField()),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.flight')),
            ],
        ),
    ]