from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/cowboy', views.cowboy_api, name='cowboy_api'),
]
