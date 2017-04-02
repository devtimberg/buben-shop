from rest_framework import routers
from shop import views as shop_view

api_router = routers.DefaultRouter()
api_router.register(r'cart', shop_view.CartViewSet, 'Cart')
api_router.register(r'update', shop_view.CartUpdateViewSet, 'Update')
api_router.register(r'delete', shop_view.CartDeleteViewSet, 'Delete')
