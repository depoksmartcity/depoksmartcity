from django.urls import path
from .views import index, login_user, register_user

app_name = 'homepage'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
]