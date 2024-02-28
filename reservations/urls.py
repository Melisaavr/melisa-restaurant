# reservations/urls.py

from django.urls import path
from .views import reservation_form, reservation_success, handle_form_submission, view_reservation, cancel_reservation

urlpatterns = [
    path('', reservation_form, name='reservation_form'),
    path('success/', reservation_success, name='reservation_success'),
    path('handle_form_submission/', handle_form_submission, name='handle_form_submission'),
    path('view_reservation/', view_reservation, name='view_reservation'),
    path('cancel_reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),  # Eklediğimiz satır
]
