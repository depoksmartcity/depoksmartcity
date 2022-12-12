from django.urls import path
from .views import show_main, registrasi, show_healthFacility, show_healthFacility_json, show_appointment_json, create_appointment, delete_appointment, show_registered_patient_page, get_appointment_flutter_json_by_userId, get_patient_flutter_by_userId, add_patient_flutter, add_appointment_flutter, delete_appointment_flutter

app_name = 'kesehatan'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('health-facility/', show_healthFacility, name='health-facility'),
    path('health-facility/json/', show_healthFacility_json, name="health-facility-json"),
    path('registrasi/', registrasi, name='registrasi'),
    path('create-appointment/', create_appointment, name='create-appointment'),
    path('delete-appointment/<int:id>', delete_appointment, name='delete-appointment'),
    path('registered-patient/', show_registered_patient_page, name='registered-patient'),
    path('create-appointment/json/', show_appointment_json, name='appointment-json'),
    path('create-appointment-flutter/', add_appointment_flutter, name='create-appointment-flutter'),
    path('create-appointment-flutter/<int:id>/json', get_appointment_flutter_json_by_userId, name="appointment-json-by-id"),
    path('show-patient-flutter/<int:id>/json', get_patient_flutter_by_userId, name="appointment-json-by-id"),
    path('registrasi-flutter/', add_patient_flutter, name='add-patient-appointment'),
     path('delete-appointment-flutter/<int:id>', delete_appointment_flutter, name='delete-appointment-flutter'),
]