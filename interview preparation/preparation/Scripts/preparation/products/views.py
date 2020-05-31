from django.shortcuts import render
from .models import Product


def product_view(request, id):
    data = {
        'product': Product.objects.get(id=id)
    }
    return render(request, 'product/index.html', data)
