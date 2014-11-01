from rest_framework import serializers
from main.models import Boat, Timeslot

__author__ = 'htm'


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = (
            'id',
            'name',
            'capacity'
        )


class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslot
        fields = (
            'id',
            'start_time',
            'duration',
            'availability',
            'boat'
        )