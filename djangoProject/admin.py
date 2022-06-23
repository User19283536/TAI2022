from django.contrib import admin
from .models import Repertuar, Movies, bookings, tickets


admin.site.register(Repertuar)
admin.site.register(Movies)
admin.site.register(bookings)
admin.site.register(tickets)