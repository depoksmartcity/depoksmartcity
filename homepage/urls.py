from django.urls import path
from .views import index, register_user

app_name = 'homepage'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_user, name='register'),
]