from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import cache_page

@login_required(login_url='/user/login.html')
@permission_required(perm='index.visit_Product', login_url='/user/login.html')

def index(request):
    product = request.GET.get('product', '')
    price = request.GET.get('price', '')
    if product:
        product_list = request.session.get('product_info', [])
        if product not in product_list:
            product_list.append({'price': price, 'product': product, })
        request.session['product_info'] = product_list
        return redirect('/')
    return render(request, 'index.html', locals())

@cache_page(timeout=10, cache='MyDjango', key_prefix='MyDjangoView')
@login_required(login_url='/user/login.html')
def ShoppingCarView(request):
    pass
    return render(request, 'ShoppingCar.html', locals())

