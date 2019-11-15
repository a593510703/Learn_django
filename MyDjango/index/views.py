from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import Product

def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name', 'type')
    # context = {
    #     'title': '首页',
    #     'type_list': type_list,
    #     'name_list': name_list,
    # }
    title = '首页'
    return render(request, 'index.html', context=locals(), status=200)

def login(request):
    return redirect('/')
