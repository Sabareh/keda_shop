from django.shortcuts import render
from .models import Product

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def store(request,):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)