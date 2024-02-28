from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField(choices=[(i, i) for i in range(1, 5)])  # guests alanı 1 ila 4 arasında seçenekler içerecek

    class Meta:
        app_label = 'reservations'
