from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'guests_count')  # guests_count ekledik

    def guests_count(self, obj):
        return obj.guests

admin.site.register(Reservation, ReservationAdmin)