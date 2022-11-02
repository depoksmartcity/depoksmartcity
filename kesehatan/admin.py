from django.contrib import admin
from kesehatan.models import Appointment, HealthFacility, Patient

admin.site.register(HealthFacility)
admin.site.register(Patient)
admin.site.register(Appointment)