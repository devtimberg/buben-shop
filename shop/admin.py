from django.contrib import admin
from shop import models as shop_models


class PhotoInline(admin.TabularInline):
    model = shop_models.PhotoProduct
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


admin.site.register(shop_models.Categories)
admin.site.register(shop_models.Order)
admin.site.register(shop_models.ProductInCart)
admin.site.register(shop_models.Product, ProductAdmin)
