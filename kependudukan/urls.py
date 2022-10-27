from django.urls import path
from kependudukan.views import show_kependudukan, show_request_ktp, show_json, show_request_ktp_json

app_name = 'kependudukan'

urlpatterns = [
    path('', show_kependudukan, name='show_kependudukan'),
    path('request-ktp', show_request_ktp, name='show_request_ktp'),
    path('json', show_json, name='show_json'),
    path('request-ktp/json', show_request_ktp_json, name='show_request_ktp_json'),
]