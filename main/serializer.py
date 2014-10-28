from rest_framework import serializers
from main.models import Boat

__author__ = 'htm'

class BoatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boat
        fields = ('name_of_boat', 'capacity')