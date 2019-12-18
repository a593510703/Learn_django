from django.urls import path, re_path
from . import views

urlpatterns = [
    path('findPassword.html', views.findPassword, name='findPassword'),
    path('login.html', views.loginView, name='login'),
    path('register.html', views.registerView, name='register'),
    path('setpassword.html', views.setpasswordView, name='setpassword'),
    path('logout.html', views.logoutView, name='logout'),
]