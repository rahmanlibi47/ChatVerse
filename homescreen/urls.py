from django.urls import path
from .views import homescreen

urlpatterns = [
    path('', homescreen, name='homescreen'),
    # other URL patterns...
]
