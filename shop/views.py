from django.views import generic
from shop import models as shop_models


class IndexShopView(generic.TemplateView):
    template_name = 'shop/shop_index.html'


class ShopListView(generic.ListView):
    template_name = 'shop/shop_list.html'
    model = shop_models.Product