from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import Product
from django.views.generic import ListView

def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
    context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
    return render(request, 'index.html', context=context, status=200)