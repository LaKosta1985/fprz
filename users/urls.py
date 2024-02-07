
from django.urls import path
from users import views
from django.conf import settings


urlpatterns = [
    path('registration/', views.registration,name='registration'),  
    path('login/', views.login,name='login'),  
    path('profile/', views.profile,name='profile'), 
    path('logout/', views.logout,name='logout'), 
]