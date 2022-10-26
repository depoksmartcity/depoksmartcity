from django.urls import path
from restaurants.views import show_restaurants
from restaurants.views import show_json

app_name = 'restaurants'

urlpatterns = [
    path('', show_restaurants, name='restaurants'),
    path('json/', show_json, name='json')

]