from django.urls import path
from .views import *

urlpatterns = [
    path('login/', signin, name='accounts_signin'),
    path('register/', register, name='accounts_register'),
    path('engineer_register/', engineer_register, name='accounts_engineer_register'),
    path('profile/', edit_customer, name='accounts_profile'),
    path('change_password/', change_password, name='accounts_change_password'),
    path('logout/', logout_action, name='accounts_logout')
]