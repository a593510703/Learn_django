from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import Product
from django.views.generic import ListView

class ProductList(ListView):
    context_object_name = 'type_list'
    template_name = 'index_view.html'
    queryset = Product.objects.values('type').distinct()

    def get_queryset(self):
        print(self.kwargs['id'])
        print(self.kwargs['name'])
        print(self.request.method)
        type_list = Product.objects.values('type').distinct()
        return type_list
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name', 'type')
        return context