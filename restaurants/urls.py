from django.urls import path
from restaurants.views import show_restaurants
from restaurants.views import show_json
from restaurants.views import review_json
from restaurants.views import create_review

app_name = 'restaurants'

urlpatterns = [
    path('', show_restaurants, name='restaurants'),
    path('json/', show_json, name='json'),
    path('json-rev/<int:pk>', review_json, name='rev_json'),
    path('create-review/', create_review, name='create-review')
]