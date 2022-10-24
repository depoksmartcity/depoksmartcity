from django.urls import path
from kependudukan.views import show_kependudukan, show_request_ktp

app_name = 'kependudukan'

urlpatterns = [
    path('', show_kependudukan, name='show_kependudukan'),
    path('request-ktp', show_request_ktp, name='show_request_ktp'),
]