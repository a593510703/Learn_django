"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
urlpatterns = [
    # 首页的URL
    path('', views.index, name='index'),
    # 购物车
    path('ShoppingCar.html', views.ShoppingCarView, name='ShoppingCar'),
    # path('message.html', views.messageView, name='message'),
    path('pagination/<int:page>.html', views.paginationView, name='pagination'),
]
