from django.shortcuts import render

# Create your views here.

from main.models import Boat, Timeslot
from main.serializer import BoatSerializer, TimeslotSerializer
from rest_framework import generics


def home(request):
    return render(request, 'home.html')


class BoatList(generics.ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class TimeslotList(generics.ListCreateAPIView):
    queryset = Timeslot.objects.all()
    serializer_class = TimeslotSerializer


class TimeslotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timeslot.objects.all()
    serializer_class = TimeslotSerializer