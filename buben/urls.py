from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from shop.router import api_router


urlpatterns = [
    url(r'^', include('shop.urls', namespace='shop')),

    url(r'^api/', include(api_router.urls)),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)