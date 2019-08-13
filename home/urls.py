from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('mail', views.welcome_page, name='mail')
]