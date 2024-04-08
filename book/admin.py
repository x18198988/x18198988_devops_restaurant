from django.contrib import admin
from .models import Typ, Table, Booking
# Register your models here.

admin.site.register(Typ)
admin.site.register(Table)
admin.site.register(Booking)