from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import Product
from django.views.generic import ListView
from .form import *

def index(request):
    username =request.user.username
    return render(request, 'index.html', locals())
    
def model_index(request, id):
    if request.method == 'GET':
        instance = Product.objects.filter(id=id)
        if instance:
            product = ProductModelForm(instance=instance[0])
        else:
            product = ProductModelForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            weight = product.cleaned_data['weight']
            product_db = product.save(commit=False)
            product_db.name= '我的 iPhone'
            product_db.save()
            return HttpResponse('提交成功！weight清洗后的数据为: ' + weight)
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())