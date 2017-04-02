from django.shortcuts import get_object_or_404
from django.views import generic
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from shop import models as shop_models
from shop import forms as shop_forms
from shop import serializers as shop_serializers
from rest_framework.response import Response
from rest_framework import status


class IndexTemplateView(generic.TemplateView):
    template_name = 'shop/index_shop.html'


class CartTemplateView(generic.TemplateView):
    template_name = 'shop/cart.html'


class ProductListView(generic.ListView):
    template_name = 'shop/list_product.html'
    paginate_by = 5
    queryset = shop_models.Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = shop_models.Categories.objects.all()

        if self.request.GET:
            context['form'] = shop_forms.FilterForm(self.request.GET)
        else:
            context['form'] = shop_forms.FilterForm
        return context

    def get_queryset(self):
        queryset = shop_models.Product.objects.filter()
        ftr = self.request.GET
        if ftr.get('min_price'):
            queryset = queryset.filter(price__gte=ftr.get('min_price'))
        if ftr.get('max_price'):
            queryset = queryset.filter(price__lte=ftr.get('max_price'))
        return queryset


class ProductDetailView(generic.DetailView):
    template_name = 'shop/detail_product.html'
    model = shop_models.Product
    context_object_name = 'product'


class CategoryList(generic.ListView):
    template_name = 'shop/list_category.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['categories'] = shop_models.Categories.objects.all()
        context['category'] = get_object_or_404(shop_models.Categories, slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        category = get_object_or_404(shop_models.Categories, slug=self.kwargs['slug'])
        self.category = category
        queryset = shop_models.Product.objects.filter(category=self.category)
        ftr = self.request.GET
        if ftr.get('min_price'):
            queryset = queryset.filter(price__gte=ftr.get('min_price'))
        if ftr.get('max_price'):
            queryset = queryset.filter(price__lte=ftr.get('max_price'))
        return queryset


class CartViewSet(viewsets.ModelViewSet):
    queryset = shop_models.Cart.objects.all()
    serializer_class = shop_serializers.CartSerializer


    def list(self, request, *args, **kwargs):
        cart, created = shop_models.Cart.objects.get_or_create(session=request.session.session_key)
        return Response({'status': True,
                         'cart': shop_serializers.CartSerializer(cart).data,
                         },
                        status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        cart, created = shop_models.Cart.objects.get_or_create(session=request.session.session_key)
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product = get_object_or_404(shop_models.Product, pk=product_id)
        pic = cart.productincart_set.filter(product=product).first()
        if pic:
            pic.quantity += int(quantity)
            pic.save()
        else:
            shop_models.ProductInCart.objects.create(
                product=product, quantity=quantity, cart=cart)

        return Response({'status': True,
                         'cart': shop_serializers.CartSerializer(cart).data
                         },
                        status=status.HTTP_200_OK)


class CartUpdateViewSet(viewsets.ModelViewSet):
    queryset = shop_models.ProductInCart.objects.all()
    serializer_class = shop_serializers.ProductInCartSerializer

    def update(self, request, pk=None, *args, **kwargs):
        cart, created = shop_models.Cart.objects.get_or_create(session=request.session.session_key)
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product = get_object_or_404(shop_models.Product, pk=product_id)
        pic = cart.productincart_set.filter(product=product).first()
        if pic:
            pic.quantity = int(quantity)
            pic.save()

        return Response({'status': True,
                         'cart': shop_serializers.CartSerializer(cart).data},
                        status=status.HTTP_200_OK)


class CartDeleteViewSet(viewsets.ModelViewSet):
    queryset = shop_models.ProductInCart.objects.all()
    serializer_class = shop_serializers.ProductInCartSerializer

    def destroy(self, request, *args, **kwargs):
        cart, created = shop_models.Cart.objects.get_or_create(session=request.session.session_key)
        product_id = request.POST.get('product_id')
        product = get_object_or_404(shop_models.Product, pk=product_id)
        pic = cart.productincart_set.filter(product=product).first()
        if pic:
            pic.delete()

        return Response({'status': True,
                         'cart': shop_serializers.CartSerializer(cart).data
                         },
                        status=status.HTTP_200_OK)


