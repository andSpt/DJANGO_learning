from django.shortcuts import render
from django.http import HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from users.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    context = {'title': 'Store',}
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'Store - Каталог',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required()
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

