
from django.db import models
from math import log
from config.configs import TANK, PASS_CONSUMPTION, FUEL_CONS


# Check this model against intruction

class Plane(models.Model):
    plane_name = models.CharField(max_length=100,null=False, blank=False)
    id_by_user = models.IntegerField(null=False, blank=False)
    passenger_capacity = models.IntegerField(null=False, blank=False)
    cons_per_mnt = models.FloatField(editable=False, null=False)
    tot_cons_per_minute = models.FloatField(editable=False,null=False)
    max_flight_time = models.FloatField(editable=False,null=False)
    fuel_cap = models.IntegerField(editable=False,null=False)
    max_pass_consumption = models.FloatField(editable=False,null=False)
    created_date = models.DateField(auto_now_add=True,null=False)


    def save(self, *args, **kwargs)-> None:
        # Calculate values for the new columns based on other columns
        self.fuel_cap = self.id_by_user * TANK
        self.cons_per_mnt = log(self.id_by_user) * FUEL_CONS
        self.max_pass_consumption = self.passenger_capacity * PASS_CONSUMPTION
        self.tot_cons_per_minute = self.cons_per_mnt + self.max_pass_consumption
        self.max_flight_time  = self.fuel_cap/self.tot_cons_per_minute
        super().save(*args, **kwargs)