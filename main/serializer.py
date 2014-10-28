from rest_framework import serializers
from main.models import Boat

__author__ = 'htm'


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = (
            'id',
            'name_of_boat',
            'capacity'
        )