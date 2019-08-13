from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login, name='login'),
    path('profile', views.ProfileUpdate.as_view(), name='profile'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIAFILES_LOCATION, document_root=settings.DEFAULT_FILE_STORAGE)