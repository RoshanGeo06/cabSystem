# Generated by Django 4.1 on 2022-11-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0009_remove_destination_vehicle_remove_drivers_attendees_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='vehicle',
            field=models.ManyToManyField(blank=True, to='cab.vehicle'),
        ),
    ]
