from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login.html', views.login),
    
]