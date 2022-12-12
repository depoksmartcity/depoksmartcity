from django.urls import path
from .views import index, login_user, register_user, logout_user, login_flutter, register_flutter, logout_flutter

app_name = 'homepage'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('logout-flutter/', logout_flutter, name='logout_flutter'),
    path('login-flutter/', login_flutter, name='login_flutter'),
    path('register-flutter/', register_flutter, name='register_flutter'),

]