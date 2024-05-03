from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeLoader, name='MyHome')
]
