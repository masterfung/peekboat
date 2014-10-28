from django.contrib import admin

# Register your models here.
from main.models import Boat, Timeslot


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    pass


@admin.register(Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    pass

