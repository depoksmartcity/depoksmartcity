from django.urls import path
from aspirasi.views import show_aspirasi, show_json, add_aspirasi_ajax, show_aspirasi_pendatang

app_name = 'aspirasi'

urlpatterns = [
    path('', show_aspirasi, name='show_aspirasi'),
    path('json/', show_json, name='show_json'),
    path('add/', add_aspirasi_ajax, name='add_aspirasi_ajax'),
    path('show-aspirasi/', show_aspirasi_pendatang, name='show_aspirasi_pendatang'),

]