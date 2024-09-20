from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def product_list(request):
    return render(request, 'app/products.html')

def product_detail(request):
    return render(request, 'app/single-product.html')