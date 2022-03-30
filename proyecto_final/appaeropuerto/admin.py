from django.contrib import admin
from appaeropuerto.models import Avion, Empleado, Pasajero

# Register your models here.

admin.site.register(Avion)
admin.site.register(Empleado)
admin.site.register(Pasajero)