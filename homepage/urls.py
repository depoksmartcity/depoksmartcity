from django.urls import path
from .views import index, register_user, login_user, logout_user

app_name = 'homepage'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]