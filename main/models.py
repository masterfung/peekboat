from django.db import models

# Create your models here.


class Boat(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(max_length=3)

    def __unicode__(self):
        return "{} has {} as its max capacity.".format(self.name,
                                                       self.capacity)


class Timeslot(models.Model):
    start_time = models.DateField()
    duration = models.IntegerField(max_length=3)
    availability = models.IntegerField(default=0)
    boat = models.ForeignKey(Boat, related_name='boat', default=None, null=True, blank=True)

    def __unicode__(self):
        return "start time: {}, duration: {}".format(self.start_time, self.duration)


# class Assignment(models.Model):
#     boat = models.ForeignKey(Boat, related_name='boat')
#
#     def __unicode__(self):
#         return self.boat