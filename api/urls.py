from django.urls import path

from .views import register, user_settings


urlpatterns = [
    path('users/register', register, name='register'),
    path('users/settings', user_settings, name='settings'),
]
