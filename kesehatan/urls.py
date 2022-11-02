from django.urls import path
from .views import show_main, registrasi, show_healthFacility, show_healthFacility_json, show_appointment_json, create_appointment

app_name = 'kesehatan'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('health-facility/', show_healthFacility, name='health-facility'),
    path('health-facility/json/', show_healthFacility_json, name="health-facility-json"),
    path('registrasi/', registrasi, name='registrasi'),
    path('create-appointment/json/', show_appointment_json, name='appointment-json'),
    path('create-appointment/', create_appointment, name='create-appointment'),
]