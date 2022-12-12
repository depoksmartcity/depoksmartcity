from django.urls import path
from aspirasi.views import show_aspirasi, show_json, add_aspirasi_ajax, show_aspirasi_pendatang, show_json_user, show_json_user, show_aspirasi_user, add_aspirasi_flutter

app_name = 'aspirasi'

urlpatterns = [
    path('', show_aspirasi, name='show_aspirasi'),
    path('json/', show_json, name='show_json'),
    path('add/', add_aspirasi_ajax, name='add_aspirasi_ajax'),
    path('show-aspirasi/', show_aspirasi_pendatang, name='show_aspirasi_pendatang'),
    path('json-user/', show_json_user, name='show_json_user'),
    path('aspirasi-user/', show_aspirasi_user, name='show_aspirasi_user'),
    path('add-aspirasi-flutter/', add_aspirasi_flutter, name='show_aspirasi_flutter'),



]

