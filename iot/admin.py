from django.contrib import admin
from .models import *

admin.site.register(Variable)
admin.site.register(Lectura)
admin.site.register(Sensor)
admin.site.register(Nodo)
admin.site.register(Ubicacion)
admin.site.register(Tipo_nodo)
admin.site.register(Tipo_sensor)
admin.site.register(Tipo_ubicacion)
