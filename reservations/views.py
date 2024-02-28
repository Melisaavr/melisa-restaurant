# reservations/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation

def reservation_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            # Form başarıyla gönderildiğinde ana sayfaya yönlendir
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})

def reservation_success(request):
    # Son eklenen rezervasyonu al
    latest_reservation = Reservation.objects.latest('id')
    return render(request, 'reservation_success.html', {'reservation': latest_reservation})

def handle_form_submission(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect('reservation_success')

    return render(request, 'reservation_form.html', {'form': ReservationForm()})

def view_reservation(request):
    searched_name = None
    reservations = None

    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            # İsimle eşleşen rezervasyonları getir
            reservations = Reservation.objects.filter(name__iexact=name)
            searched_name = name
    else:
        # Eğer POST isteği değilse, tüm rezervasyonları getir
        reservations = Reservation.objects.all()

    return render(request, 'view_reservation.html', {'reservations': reservations, 'searched_name': searched_name})

def cancel_reservation(request, reservation_id):
    # İlgili rezervasyonu bul
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        # E-posta doğrulama işlemleri buraya eklenebilir

        # Rezervasyonu iptal et
        reservation.delete()
        return redirect('view_reservation')

    return render(request, 'cancel_reservation.html', {'reservation': reservation})
