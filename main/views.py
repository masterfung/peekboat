from django.shortcuts import render

# Create your views here.

from main.models import Boat
from main.serializer import BoatSerializer
from rest_framework import generics


class BoatList(generics.ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer