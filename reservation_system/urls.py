
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/', include('reservations.urls')),
    path('', include("home.urls"))
]

# from django.urls import path
# from reservations.views import reservation_form, reservation_success

# urlpatterns = [
#     path('', reservation_form, name='reservation_form'),
#     path('success/', reservation_success, name='reservation_success'),
# ]
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('reservations.urls')),
# ]

# from django.urls import path



