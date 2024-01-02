from django.contrib import admin
from . models import Plane


# Register your models here.
class PlaneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "plane_name",
        "id_by_user",
        "passenger_capacity",
        "cons_per_mnt",
        "tot_cons_per_minute",
        "max_flight_time",
        "fuel_cap",
        "max_pass_consumption",
        "created_date",
    )
    list_display_links = ("id", "plane_name", "passenger_capacity")
    search_fields = ("id", "plane_name", "passenger_capacity")
    list_filter = ("id", "plane_name", "passenger_capacity")
    

    fieldsets = (
        ('Editable Fields', {
            'fields': (
                "plane_name",
                "id_by_user",
                "passenger_capacity",
            ),
        }),
        ('Non-Editable Fields', {
            'fields': (
                "cons_per_mnt",
                "tot_cons_per_minute",
                "max_flight_time",
                "fuel_cap",
                "max_pass_consumption",
            ),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('cons_per_mnt', 'tot_cons_per_minute', 'max_flight_time', 'fuel_cap', 'max_pass_consumption', "created_date",)

admin.site.register(Plane,PlaneAdmin)
