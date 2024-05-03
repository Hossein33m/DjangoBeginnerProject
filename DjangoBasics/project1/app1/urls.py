from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpLoader, name='MySignUp'),
    path('color/', views.ColorLoader, name='MyColor'),
]
