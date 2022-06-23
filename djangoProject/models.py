from django.db import models
import datetime

from django.db.models import SET_NULL
from django.utils import timezone
from django.contrib.auth.models import User


class Movies(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    title = models.CharField(max_length=60)
    type = models.CharField(max_length=30)
    duration = models.IntegerField()
    primetime = models.DateField()
    director = models.CharField(max_length=80)
    writing = models.CharField(max_length=80)
    crew = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    path = models.CharField(max_length=50, null=True)


class Repertuar(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    t_id = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True)
    date1 = models.DateTimeField(null=True)
    av_tickets1 = models.IntegerField(null=False, default=50)
    date2 = models.DateTimeField(null=True)
    av_tickets2 = models.IntegerField(null=False, default=50)
    date3 = models.DateTimeField(null=True)
    av_tickets3 = models.IntegerField(null=False, default=50)
    date4 = models.DateTimeField(null=True)
    av_tickets4 = models.IntegerField(null=False, default=50)

    class Meta:
        ordering = ('-id',)

class bookings(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    r_id = models.ForeignKey(Repertuar, on_delete=SET_NULL, null=True)
    email = models.CharField(max_length=50, null=True)
    data_rezerwacji = models.DateTimeField(auto_now_add=True, blank=True)
    normalny = models.IntegerField(null=False, default=0)
    ulgowy = models.IntegerField(null=False, default=0)
    szkolny = models.IntegerField(null=False, default=0)
    rodzinny = models.IntegerField(null=False, default=0)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(null=True)
    naleznosc = models.FloatField(null=False, default=0)

class tickets(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    type = models.CharField(max_length=50)
    price = models.FloatField(null=False, default=19.90)