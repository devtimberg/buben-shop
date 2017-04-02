from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Category'))
    slug = models.SlugField(verbose_name=_('URL'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    category = models.ForeignKey(Categories, verbose_name=_('Category product'))
    name = models.CharField(max_length=200, verbose_name=_('Name product'))
    slug = models.SlugField(verbose_name=_('URL'))
    image = ThumbnailerImageField(upload_to='product', blank=True, verbose_name=_('Image product'))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Price product'))
    description = models.TextField(verbose_name=_('Description product'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return str(self.name)

    def get_image(self):
        return self.photoproduct_set.all()


class PhotoProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('Product name'))
    image = ThumbnailerImageField(upload_to='product', blank=True, verbose_name=_('Photo product'))

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    def __str__(self):
        return str(self.product)


class Cart(models.Model):
    session = models.CharField(max_length=255)

    def __str__(self):
        return str(self.session)


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))
    cart = models.ForeignKey(Cart, null=True, blank=True)


class Order(models.Model):
    session = models.CharField(max_length=255)
    email = models.EmailField(max_length=11, null=True, verbose_name=_('Email'))
    product = models.ManyToManyField(Product, related_name='order_product', verbose_name=_('Product'))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Price'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


