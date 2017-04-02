from django.conf.urls import url
from shop import views as shop_view

urlpatterns = [
    url(r'^$', shop_view.IndexTemplateView.as_view(), name='index_shop'),
    url(r'^shop/$', shop_view.ProductListView.as_view(), name='list_product'),
    url(r'^shop/(?P<slug>[-\w]+)/$', shop_view.ProductDetailView.as_view(), name='detail_product'),
    url(r'^shop/category/(?P<slug>[-\w]+)/$', shop_view.CategoryList.as_view(), name='list_category'),

    url(r'^cart/$', shop_view.CartTemplateView.as_view(), name='cart'),
]
