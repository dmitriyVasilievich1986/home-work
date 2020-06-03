from django.urls import path
from .views import (
    product_view,
    new_product
)

urlpatterns = [
    path('', product_view, name="product"),
    path('<int:id>', product_view, name="product"),
    path('new/', new_product)
]