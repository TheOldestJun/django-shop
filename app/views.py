from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app/index.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app/products.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, 'app/single-product.html', context)