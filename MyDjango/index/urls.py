from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    # path('<int:id>.html', views.model_index),
    path('ShoppingCar.html', views.ShoppingCarView, name='ShoppingCar'),
]