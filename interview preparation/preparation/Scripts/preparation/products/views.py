from django.shortcuts import render
from .models import Product
from .form import ProductForm


def product_view(request, id=0):
    data = {
        'product': [Product.objects.get(id=id)] if id else Product.objects.all()
    }
    return render(request, 'product/index.html', data)

def new_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        Product.objects.create(**form.cleaned_data)
        form = ProductForm()
    data = {
        'form': form
    }
    return render(request, "product/Form.html", data)