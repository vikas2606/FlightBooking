# Generated by Django 4.1.3 on 2022-12-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_flightdetails_flight_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightdetails',
            name='flight_id',
        ),
        migrations.AddField(
            model_name='flightdetails',
            name='flight_id',
            field=models.ManyToManyField(to='adminapp.flight'),
        ),
    ]