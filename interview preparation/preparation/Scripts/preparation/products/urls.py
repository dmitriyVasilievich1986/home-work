# from django.urls import path
from rest_framework import routers
from .api import ProductViewSet
# from .views import (
#     product_view,
#     new_product
# )

# urlpatterns = [
#     path('', product_view, name="product"),
#     path('<int:id>', product_view, name="product"),
#     path('new/', new_product)
# ]

router = routers.DefaultRouter()
router.register('api/products', ProductViewSet, 'Product')
urlpatterns = router.urls