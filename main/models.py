from django.db import models

# Create your models here.


class Boat(models.Model):
    name_of_boat = models.CharField(max_length=100)
    capacity = models.IntegerField(max_length=3)

    def __unicode__(self):
        return "{} has {} as its max capacity.".format(self.name_of_boat,
                                                       self.capacity)


# class Timeslot(models.Models):
#