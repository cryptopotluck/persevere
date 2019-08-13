from django.urls import path
from . import views

urlpatterns = [
    path('', views.codingclass, name='codingclass'),
    path('employability', views.employability, name='employability'),
    path('entrepreneurship', views.entrepreneurship, name='entrepreneurship'),
    path('job-placement', views.jobplacement, name='job-placement'),
    path('life-skills', views.lifeskills, name='life-skills'),
    path('work-experience', views.workexperience, name='work-experience'),
    path('donation', views.donate, name='donation'),
    path('about', views.about, name='about')
]