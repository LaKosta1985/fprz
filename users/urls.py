
from django.urls import path
from users.views import *
from django.conf import settings


urlpatterns = [
    path('registration/', registration,name='registration'),
    path('login/', login,name='login'),  
    path('profile/',profile,name='profile'), 
    path('logout/',logout,name='logout'), 
    path('sendMesToEmail/',sendMesToEmail,name='sendMesToEmail'), 
]