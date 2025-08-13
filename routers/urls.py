from django.urls import path
from .views import home, uzbekistan, jahon


urlpatterns = [
        path('', home, name='home'),
        path('uzbekistan/', uzbekistan, name='uzbekistan'),
        path('jahon/', jahon, name='jahon')
]
