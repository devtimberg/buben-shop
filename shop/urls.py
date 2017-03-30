from django.conf.urls import url
from shop import views as shop_view

urlpatterns = [
    url(r'^$', shop_view.IndexShopView.as_view(), name='index_shop'),
    url(r'^shop/$', shop_view.ShopListView.as_view(), name='list_shop'),


]
